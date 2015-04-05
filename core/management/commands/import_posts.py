from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from facepy import GraphAPI
from core.models import Member, Post
from getenv import env
from dateutil import parser as dateparser
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
    help = 'Imports posts from Facebook'


    def get_likes_of_post(self, postid):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        likes_arr = graph.get('{}/likes?limit=1000'.format(postid))
        return len(likes_arr['data'])


    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        feed = graph.get('{}/feed?limit=500'.format(group_id))
        one_month_ago = datetime.today() - timedelta(days=30)
        tashkentzone = pytz.timezone("Asia/Tashkent")

        new_posts = 0
        while 'data' in feed and feed['data'] and \
              len(feed['data']) > 0:

            for post in feed['data']:

                print post

                postid = post['id']
                postmsg = post['message'] if 'message' in post else ''
                postctime = post['created_time']
                postutime = post['updated_time']
                creatorid = post['from']['id']
                creatorname = post['from']['name']

                ppostctime = dateparser.parse(postctime)
                # this_post_is_new =  ppostctime.replace(tzinfo=tashkentzone) > one_month_ago.replace(tzinfo=tashkentzone)

                # if this_post_is_new:
                howmanylikes = self.get_likes_of_post(postid)

                post_exists = Post.objects.filter(id=postid).exists()
                member_exists = Member.objects.filter(id=creatorid).exists()

                if not post_exists:
                    if not member_exists:
                        creator = Member.objects.create(
                            pk=creatorid,
                            name=creatorname
                        )
                    else:
                        creator = Member.objects.get(id=creatorid)

                    try:
                        Post.objects.create(
                            pk=postid,
                            message=postmsg,
                            created_time=postctime,
                            updated_time=postutime,
                            creator=creator,
                            likes=howmanylikes
                        )
                        new_posts += 1
                    except:
                        new_posts -= 1

                else:
                    # if this_post_is_new:
                    Post.objects.filter(id=postid).update(likes=howmanylikes)

            newUrl = feed['paging']['next'].replace(
                    'https://graph.facebook.com/', ''
                    )
            feed = graph.get(newUrl)


        print 'Total {0} posts added.'.format(new_posts)
