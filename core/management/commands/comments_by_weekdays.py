# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Member, Post, Comment
from django.db.models import Count, Max, Min, Avg
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import Context, loader


class Command(BaseCommand):
    help = 'Render chart for posts'

    def handle(self, *args, **options):
        comments_by_weekdays = Comment.objects.extra({
            "weekday": "EXTRACT('dow' FROM created_time AT TIME ZONE 'UZT')"
            }).values("weekday").order_by("weekday").annotate(num_comments=Count("id"))
        for comment in comments_by_weekdays:
            print comment["weekday"], comment["num_comments"]
