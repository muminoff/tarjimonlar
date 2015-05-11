from django.core.management.base import BaseCommand
from facepy import GraphAPI
from facepy.exceptions import FacebookError
from getenv import env
from core.models import Post
from redis import Redis
from time import time


class Command(BaseCommand):
    help = 'Imports members from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        # members = graph.get('{}/members?limit=1000'.format(group_id))
        for post in Post.objects.all():
            try:
                graph.get('{}'.format(post.id))
            except FacebookError:
                print 'Post {} does not exist in API, so making it false ...'.format(post.id)
                post.exists_in_group = False
                post.save()
                print '[OK]'
            else:
                print 'Post {} is OK'.format(post.id)
