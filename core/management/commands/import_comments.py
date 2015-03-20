from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from facepy import GraphAPI
from core.models import Member, Post, Comment
from getenv import env
from dateutil import parser as dateparser
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
    help = 'Imports posts from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'

        new_comments = 0
	one_month_ago = datetime.today() - timedelta(days=30)
	tashkentzone = pytz.timezone("Asia/Tashkent")
        for post in Post.objects.filter(updated_time__gte=one_month_ago.replace(tzinfo=tashkentzone)):
            comments = graph.get('{}/comments?limit=1000'.format(post.id))

            for c in comments['data']:
                commentid = c['id']
                commentcreatorid = c['from']['id']
                commentcreatorname = c['from']['name']
                commentmsg = c['message']
                commentctime = c['created_time']
                commentlikecount = c['like_count']

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
                            post=post,
                            likes=commentlikecount
                        )
                        new_comments += 1
                    except:
                        new_comments -= 1

                else:
                    Comment.objects.filter(id=commentid).update(likes=commentlikecount)

        print 'Total {0} comments added.'.format(new_comments)
