# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Member, Post, Comment

class Command(BaseCommand):
    help = 'Show group feed'

    def handle(self, *args, **options):
        # print '\nShowing last 10 posts creations...\n'
        # print '----------------------------------\n'
        # last_ten_posts = Post.objects.order_by('-created_time')[:10]
        
        # for post in last_ten_posts:
        #     print u'Иштирокчи {creator} {when_date} куни соат {when_time} да пост ёзди {post_link}.'.format(
        #             creator=post.creator.name,
        #             when_date=post.created_time.strftime('%d-%m-%Y'),
        #             when_time=post.created_time.strftime('%X'),
        #             post_link='https://fb.com/'+post.id
        #             )

        # print '----------------------------------\n'

        print '\nShowing last 10 comments creations...\n'
        print '----------------------------------\n'
        last_ten_comments = Comment.objects.order_by('-created_time')[:10]
        
        for comment in last_ten_comments:
            print u'Иштирокчи {creator} {when_date} куни соат {when_time} да шарҳ ёзди {comment_link}.'.format(
                    creator=comment.creator.name,
                    when_date=comment.created_time.strftime('%d-%m-%Y'),
                    when_time=comment.created_time.strftime('%X'),
                    comment_link='https://fb.com/'+comment.id
                    )

        print '----------------------------------\n'
