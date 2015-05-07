from django.core.management.base import BaseCommand
from facepy import GraphAPI
from getenv import env
from core.models import Member


class Command(BaseCommand):
    help = 'Imports members from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        members = graph.get('{}/members?limit=1000'.format(group_id))

        current_members = list()
        print "Getting current members from API ..."

        while 'data' in members and members['data'] and \
              len(members['data']) > 0:

            for member in members['data']:
                current_members.append(member['id'])

            newUrl = members['paging']['next'].replace(
                'https://graph.facebook.com/', ''
            )
            members = graph.get(newUrl)

        print "Currently {} members fetched from Facebook API".format(len(current_members))

        for member_in_db in Member.objects.all():
            if member_in_db.id in current_members:
                member_in_db.currently_member = True
                member_in_db.save()

        print "Currently {} members in DB".format(Member.objects.filter(currently_member=True).count())
