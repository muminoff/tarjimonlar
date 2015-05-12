from django.core.management.base import BaseCommand
from facepy import GraphAPI
from facepy.exceptions import FacebookError
from getenv import env
from core.models import Comment


class Command(BaseCommand):
    help = 'Check comments from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        irrelevant_comments = list()
        relevant_comments = list()

        print "Checking comments from API ..."
        for comment in Comment.objects.all():
            try:
                graph.get('{}'.format(comment.id))
            except FacebookError:
                comment.delete()
                irrelevant_comments.append(comment.id)
            else:
                relevant_comments.append(comment.id)

        print "Irrelevant comments {}, and relevant comments {}".format(len(irrelevant_comments), len(relevant_comments))
