from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from facepy import GraphAPI
from core.models import Member, Post, Comment
from getenv import env

def if_exists(*args):
    def get(obj):
        for arg in args:
            if isinstance(obj, dict) and arg in obj:
                obj = obj[args]
            else:
                return None
        return obj
    return get

class Command(BaseCommand):
    help = 'Imports posts from Facebook'

    def get_likes_of_comment(self, commentid):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        likes_arr = graph.get('{}/likes?limit=1000'.format(commentid))
        print 'Getting like counts of {comment_id} - {like_counts}...'.format(
                comment_id=commentid,
                like_counts=len(likes_arr['data'])
                )
        return len(likes_arr['data'])

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        grab_likes = env('GRAB_LIKES')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'

        new_comments = 0
        for post in Post.objects.all():
            comments = graph.get('{}/comments?limit=1000'.format(post.id))

            for c in comments['data']:
                commentid = c['id']
                commentcreatorid = c['from']['id']
                commentcreatorname = c['from']['name']
                commentmsg = c['message']
                commentctime = c['created_time']

                if grab_likes:
                    howmanylikes = self.get_likes_of_comment(postid)
                else:
                    howmanylikes = 0

                comment_exists = Comment.objects.filter(id=c['id']).exists()
                member_exists = Member.objects.filter(id=commentcreatorid).exists()
                
                if not comment_exists:
                    if not member_exists:
                        commentcreator = Member.objects.create(
                            pk=commentcreatorid,
                            name=commentcreatorname
                        )
                    else:
                        commentcreator = Member.objects.get(
                            pk=commentcreatorid
                        )

                    try:
                        Comment.objects.create(
                            pk=commentid,
                            message=commentmsg if 'message' in c else '',
                            created_time=commentctime,
                            creator=commentcreator,
                            post=post
                        )
                        new_comments += 1
                    except:
                        new_comments -= 1

                else:
                    Comment.objects.filter(id=commentid).update(likes=howmanylikes)

        print 'Total {0} comments added.'.format(new_comments)
