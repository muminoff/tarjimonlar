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

        while 'data' in members and members['data'] and \
              len(members['data']) > 0:
            for member in members['data']:
                if not Member.objects.filter(pk=member['id']).exists():
                    picture_url = graph.get(member['id'] + '/picture?redirect=false')['data']['url']
                    try:
                        Member.objects.create(
                            pk=member['id'],
                            name=member['name'],
                            picture_url=picture_url
                        )
                        print u'{} imported'.format(member['name'])
                    except Exception, e:
                        print str(e), unicode(member['name']), member['id'], ' failed...'
                else:
                    print unicode('Member {} already exists..'.format(member['id']))

            newUrl = members['paging']['next'].replace(
                'https://graph.facebook.com/', ''
            )
            members = graph.get(newUrl)
