from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from facepy import GraphAPI
from core.models import Member
from getenv import env
import sys
import redis
import time


class Command(BaseCommand):
    help = 'Imports members from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        members = graph.get('{}/members?limit=1000'.format(group_id))
        r = redis.Redis()
        thistimestamp = int(time.time())

        while 'data' in members and members['data'] and \
              len(members['data']) > 0:
            for member in members['data']:
		r.incrby('{}:{}:members'.format(group_id, thistimestamp), 1)

            newUrl = members['paging']['next'].replace(
                'https://graph.facebook.com/', ''
            )
            members = graph.get(newUrl)

        print r.get('{}:{}:members'.format(group_id, thistimestamp))
