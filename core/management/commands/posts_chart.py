# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Member, Post, Comment
from django.db.models import Count
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader


class Command(BaseCommand):
    help = 'Render chart for posts'

    def handle(self, *args, **options):
        daily_posts = Post.objects.extra({
            "day": "date_trunc('day', created_time)"
            }).values('day').order_by('day').annotate(num_posts=Count('id'))
        monthly_posts = Post.objects.extra({
            "month": "date_trunc('month', created_time)"
            }).values('month').order_by('month').annotate(num_posts=Count('id'))
        yearly_posts = Post.objects.extra({
            "year": "date_trunc('year', created_time)"
            }).values('year').order_by('year').annotate(num_posts=Count('id'))
        context = {
            "daily_posts": daily_posts,
            "monthly_posts": monthly_posts,
            "yearly_posts": yearly_posts,
        }
        template_file = "posts_chart.js"
        template = loader.get_template(template_file)
        print render_to_response(template_file, context).content
