from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Member, Post, Comment

class Command(BaseCommand):
    help = 'Show import status'

    def handle(self, *args, **options):
        total_members = Member.objects.count()
        total_posts = Post.objects.count()
        total_comments = Comment.objects.count()

        print "\n---------------------------------\n"
        print "Total members: {}".format(total_members)
        print "Total posts: {}".format(total_posts)
        print "Total comments: {}".format(total_comments)
        print "\n---------------------------------\n"
