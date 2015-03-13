# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Member, Post, Comment
from django.db.models import Count, Max, Min, Avg, Sum
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import Context, loader


class Command(BaseCommand):
    help = 'Render chart for posts'

    def handle(self, *args, **options):
        posts_by_hours = Post.objects.extra({
            "hour": "extract('hour' from created_time at time zone 'UZT')"
            }).values("hour").order_by("hour").annotate(num_posts=Count("id"))

        posts = []
        for post in posts_by_hours:
            pobj = {}
            pobj["daytime"] = "morning" if post["hour"] < 12 and post["hour"] > 0 else "afternoon"
            pobj["hour"] = post["hour"]
            pobj["num_posts"] = post["num_posts"]
            posts.append(pobj)

        print posts
