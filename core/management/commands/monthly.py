# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Member, Post, Comment
from django.db.models import Count
from django.template.loader import render_to_string

class Command(BaseCommand):
    help = 'Show group feed'

    def handle(self, *args, **options):
        daily_comments = Comment.objects.extra({
            "day": "date_trunc('day', created_time)"
            }).values('day').order_by().annotate(num_comments=Count('id'))
        monthly_comments = Comment.objects.extra({
            "month": "date_trunc('month', created_time)"
            }).values('month').order_by().annotate(num_comments=Count('id'))
        yearly_comments = Comment.objects.extra({
            "year": "date_trunc('year', created_time)"
            }).values('year').order_by().annotate(num_comments=Count('id'))
        context = {
            "total_comments": Comment.objects.count(),
            "daily_comments": daily_comments,
            "monthly_comments": monthly_comments,
            "yearly_comments": yearly_comments,
        }
        template_file = open(settings.STATICFILES_DIRS[0] + '/js/daily_comments.js', 'w')
        render_to_string(template_file, context)


