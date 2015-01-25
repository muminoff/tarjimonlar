from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from facepy import GraphAPI
from core.models import Member, Post
from getenv import env


class Command(BaseCommand):
    help = 'Imports posts from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        feed = graph.get('{}/feed?limit=100'.format(group_id))

        while 'data' in feed and feed['data'] and \
              len(feed['data']) > 0:
            for post in feed['data']:
                postid = post['id']
                postmsg = post['message'] if 'message' in post else ''
                postctime = post['created_time']
                postutime = post['updated_time']
                creatorid = post['from']['id']
                creatorname = post['from']['name']
                post_exists = Post.objects.filter(id=postid).exists()
                member_exists = Member.objects.filter(id=creatorid).exists()
                if not post_exists:
                    print 'Post', postid, 'not exists'
                    if not member_exists:
                        print 'Member', creatorid, 'not exists'
                        creator = Member.objects.create(
                            pk=creatorid,
                            name=creatorname
                        )
                    else:
                        print 'Member', creatorid, 'exists'
                        creator = Member.objects.get(id=creatorid)
                    print 'Now creating post'
                    Post.objects.create(
                        pk=postid,
                        message=postmsg,
                        created_time=postctime,
                        updated_time=postutime,
                        creator=creator
                    )
                    print 'Post', postid, 'created'
                else:
                    print 'Post', postid, 'exists'


            newUrl = feed['paging']['next'].replace(
                'https://graph.facebook.com/', ''
            )
            feed = graph.get(newUrl)
