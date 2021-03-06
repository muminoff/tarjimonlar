from django.core.management.base import BaseCommand
from facepy import GraphAPI
from facepy.exceptions import FacebookError
from getenv import env
from core.models import Post


class Command(BaseCommand):
    help = 'Check posts from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        irrelevant_posts = list()
        relevant_posts = list()
        old_relevant_posts = Post.objects.count()
        print "Checking posts from API ..."
        for post in Post.objects.all():
            try:
                graph.get('{}'.format(post.id))
            except FacebookError:
                print "Post {} not exists in Facebook".format(post.id)
                irrelevant_posts.append(post.id)
                post.delete() 
            else:
                print "Post {} OK".format(post.id)
                relevant_posts.append(post.id)

        print "Irrelevant posts {}, and relevant posts {} (was {})".format(len(irrelevant_posts), len(relevant_posts), old_relevant_posts)
