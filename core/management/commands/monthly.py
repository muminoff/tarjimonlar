# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Member, Post, Comment
from django.db.models import Sum, Count
from django.db import connection

class Command(BaseCommand):
    help = 'Show group feed'

    def handle(self, *args, **options):
        truncate_date = connection.ops.date_trunc_sql('month', 'created_time')
        qs = Comment.objects.extra({'month': truncate_date})
        report = qs.values('month').annotate(Sum('pk'), Count('pk')).order_by('month')
        print report
