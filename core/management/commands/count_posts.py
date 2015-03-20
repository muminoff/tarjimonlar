from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from facepy import GraphAPI
from core.models import Member, Post
from getenv import env
import redis
import time


class Command(BaseCommand):
    help = 'Imports posts from Facebook'


    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        feed = graph.get('{}/feed?limit=1000'.format(group_id))
        r = redis.Redis()
        this_timestamp = int(time.time())

        while 'data' in feed and feed['data'] and \
              len(feed['data']) > 0:

            for post in feed['data']:
                r.incrby('{}:{}:posts'.format(group_id, this_timestamp), 1)

            newUrl = feed['paging']['next'].replace(
                'https://graph.facebook.com/', ''
            )
            feed = graph.get(newUrl)


        print r.get('{}:{}:posts'.format(group_id, this_timestamp))
