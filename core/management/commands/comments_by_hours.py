# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Post, Comment
from django.db.models import Count, Max, Avg
from django.shortcuts import render_to_response
from django.template import Context, loader


class Command(BaseCommand):
    help = 'Render chart for posts'

    def handle(self, *args, **options):
        comments_by_weekdays = Comment.objects.extra({
            "hour": "extract('hour' from created_time at time zone 'UZT')"
            }).values("hour").order_by("hour").annotate(num_comments=Count("id"))
        for comment in comments_by_weekdays:
            print comment["hour"], comment["num_comments"]
