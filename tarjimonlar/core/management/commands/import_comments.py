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

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        for post in Post.objects.all():
            comments = graph.get('{}/comments?limit=1000'.format(post.id))

            for c in comments['data']:
                commentid = c['id']
                commentcreatorid = c['from']['id']
                commentcreatorname = c['from']['name']
                commentmsg = c['message']
                commentctime = c['created_time']
                comment_exists = Comment.objects.filter(id=c['id']).exists()
                member_exists = Member.objects.filter(id=commentcreatorid).exists()
                
                if not comment_exists:
                    print 'Comment', commentid, 'not exists'
                    if not member_exists:
                        print 'Member', commentcreatorid, 'not exists'
                        commentcreator = Member.objects.create(
                            pk=commentcreatorid,
                            name=commentcreatorname
                        )
                    else:
                        print 'Member', commentcreatorid, 'exists'
                        commentcreator = Member.objects.get(
                            pk=commentcreatorid
                        )
                    print 'Now creating comment'
                    Comment.objects.create(
                        pk=commentid,
                        message=commentmsg if 'message' in c else '',
                        created_time=commentctime,
                        creator=commentcreator,
                        post=post
                    )
                    print 'Comment', commentid, 'created'
                else:
                    print 'Comment', commentid, 'exists'
