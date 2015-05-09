from django.core.management.base import BaseCommand
from facepy import GraphAPI
from getenv import env
from core.models import GroupMeta


class Command(BaseCommand):
    help = 'Update group info from Facebook'

    def handle(self, *args, **options):
        access_token = env('FACEBOOK_ACCESS_TOKEN')
        graph = GraphAPI(access_token)
        group_id = '438868872860349'
        api_call = graph.get('{}'.format(group_id))

        try:
            group_meta = GroupMeta.objects.get(id=group_id)
            group_meta.name = api_call['name']
            group_meta.desc = api_call['description']
            group_meta.save()
            print 'Existing group_meta updated.'

        except GroupMeta.DoesNotExist:
            group_meta = GroupMeta(id=group_id)
            group_meta.name = api_call['name']
            group_meta.desc = api_call['description']
            group_meta.save()
            print 'New group_meta created.'
