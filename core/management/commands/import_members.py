from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from facepy import GraphAPI
from core.models import Member
from getenv import env

class Command(BaseCommand):
    help = 'Imports members from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        members = graph.get('{}/members?limit=1000'.format(group_id))
        new_members = 0

        while 'data' in members and members['data'] and len(members['data']) > 0:
            for member in members['data']:
                if not Member.objects.filter(pk=member['id']).exists():
                    try:
                        Member.objects.create(
                            pk=member['id'],
                            name=member['name'],
                            admin=member['administrator'],
                        )
                        new_members += 1
                    except Exception, e:
                        new_members -= 1
                        print str(e), unicode(member['name']), member['id'], ' failed...'
                else:
                    try:
                        existing_member = Member.objects.get(pk=member['id'])
                        existing_member.name = member['name']
                        existing_member.save()
                    except Exception, e:
                        print str(e), unicode(member['name']), member['id'], ' failed...'

            newUrl = members['paging']['next'].replace(
                'https://graph.facebook.com/', ''
            )
            members = graph.get(newUrl)

        print 'Total {0} members added.'.format(new_members)
