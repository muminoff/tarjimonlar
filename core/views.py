from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db.models import Count, Sum
from django.views.decorators.cache import cache_page, never_cache
from django.contrib.auth.decorators import login_required
from core.models import Member, Post, Comment, GroupMeta
from itertools import chain
from random import sample
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from hashids import Hashids


def login_page(request):
    top_15_posters = Member.objects.annotate(
            num_posts=Count('post')).order_by('-num_posts')[:50]
    top_15_commentors = Member.objects.annotate(
            num_comments=Count('comment')).order_by('-num_comments')[:50]
    easter_egg = Member.objects.get(pk=u'10204510554222024')
    group_meta = GroupMeta.objects.all()[0]

    context = {
        "hall_of_fame": sample(
            list(chain(top_15_posters, top_15_commentors)) + [easter_egg], 100),
        "group_meta": group_meta
    }
    return render(request, 'login.html', context)


# @login_required
@cache_page(60 * 10)
def stats_page(request):
    posts_by_hours = Post.objects.filter(exists_in_group=True).extra({
        "hour": "extract('hour' from created_time at time zone 'UZT')"
        }).values("hour").order_by("-hour").annotate(num_posts=Count("id"))
    posts_by_hours_daytime = [{'hour': x['hour'], 'num_posts': x['num_posts'] } for x in posts_by_hours[11:]]
    del posts_by_hours_daytime[-1]
    posts_by_hours_nighttime = [{'hour': x['hour'], 'num_posts': x['num_posts'] } for x in posts_by_hours[:11]]
    posts_by_hours_nighttime.insert(0, {'hour': posts_by_hours.last()['hour'], 'num_posts': posts_by_hours.last()['num_posts']})

    comments_by_hours = Comment.objects.extra({
        "hour": "extract('hour' from created_time at time zone 'UZT')"
        }).values("hour").order_by("-hour").annotate(num_comments=Count("id"))
    comments_by_hours_daytime = [{'hour': x['hour'], 'num_comments': x['num_comments'] } for x in comments_by_hours[11:]]
    del comments_by_hours_daytime[-1]
    comments_by_hours_nighttime = [{'hour': x['hour'], 'num_comments': x['num_comments'] } for x in comments_by_hours[:11]]
    comments_by_hours_nighttime.insert(0, {'hour': comments_by_hours.last()['hour'], 'num_comments': comments_by_hours.last()['num_comments']})

    posts_by_weekdays = Post.objects.filter(exists_in_group=True).extra({
        "weekday": "EXTRACT('dow' FROM created_time AT TIME ZONE 'UZT')"
        }).values("weekday").order_by("weekday").annotate(num_posts=Count("id"))
    comments_by_weekdays = Comment.objects.extra({
        "weekday": "EXTRACT('dow' FROM created_time AT TIME ZONE 'UZT')"
        }).values("weekday").order_by("weekday").annotate(num_comments=Count("id"))
    posts_by_months = Post.objects.filter(exists_in_group=True).extra({
        "month": "EXTRACT('month' FROM created_time AT TIME ZONE 'UZT')"
        }).values("month").order_by("month").annotate(num_posts=Count("id"))
    comments_by_months = Comment.objects.extra({
        "month": "EXTRACT('month' FROM created_time AT TIME ZONE 'UZT')"
        }).values("month").order_by("month").annotate(num_comments=Count("id"))

    context = {
        "posts_by_hours_daytime": posts_by_hours_daytime,
        "posts_by_hours_nighttime": posts_by_hours_nighttime,
        "comments_by_hours_daytime": comments_by_hours_daytime,
        "comments_by_hours_nighttime": comments_by_hours_nighttime,
        "posts_by_weekdays": posts_by_weekdays,
        "comments_by_weekdays": comments_by_weekdays,
        "posts_by_months": posts_by_months,
        "comments_by_months": comments_by_months,
        "total_posts": Post.objects.filter(exists_in_group=True).count(),
        "total_comments": Comment.objects.count(),
    }

    return render(request, 'pages/stats_time.html', context)


# @login_required
@cache_page(60 * 10)
def members_page(request):
    non_members_count = Member.objects.filter(currently_member=False).count()
    members_count = Member.objects.filter(currently_member=True).count()
    total_members_count = non_members_count + members_count
    top_posters = Member.objects.annotate(
            num_posts=Count('post')).order_by('-num_posts')[:10]
    top_commentors = Member.objects.annotate(
            num_comments=Count('comment')).order_by('-num_comments')[:10]
    top_liked_posters = Post.objects.filter(exists_in_group=True).annotate(
            creator_times=Count('creator__name', distinct=True)).order_by('-likes')[:10]
    top_liked_commentors = Comment.objects.annotate(
            creator_times=Count('creator__name', distinct=True)).order_by('-likes')[:10]

    context = {
        "non_members_count": non_members_count,
        "members_count": members_count,
        "total_members_count": total_members_count,
        "top_posters": top_posters,
        "top_commentors": top_commentors,
        "top_liked_posters": top_liked_posters,
        "top_liked_commentors": top_liked_commentors,
    }

    return render(request, 'pages/members.html', context)


# @login_required
@cache_page(60 * 10)
def posts_page(request):
    posts_by_months = Post.objects.filter(created_time__year=2015, exists_in_group=True).extra({
        "month": "EXTRACT('month' FROM created_time AT TIME ZONE 'UZT')"
        }).values("month").order_by("month").annotate(num_posts=Count("id"))
    context = {
        "total_posts": Post.objects.filter(exists_in_group=True).count(),
        "posts_by_months": posts_by_months,
    }
    return render(request, 'pages/posts.html', context)


# @login_required
@cache_page(60 * 10)
def comments_page(request):

    context = {
        "total_comments": Comment.objects.count(),
    }
    return render(request, 'pages/comments.html', context)


class TarjimonSearchView(SearchView):
    
    def get_context_data(self, *args, **kwargs):
        context = super(TarjimonSearchView, self).get_context_data(*args, **kwargs)
        return context


# @login_required
@cache_page(60 * 10)
def subscribe_page(request):
    context = {}
    return render(request, 'pages/subscribe.html', context)


# @login_required
# @cache_page(60 * 5)
def about_page(request):
    context = {}
    return render(request, 'pages/about.html', context)


# @login_required
@cache_page(60 * 10)
def feed_page(request):
    last_ten_posts = Post.objects.filter(exists_in_group=True).order_by('-created_time')[:20]
    last_ten_comments = Comment.objects.order_by('-created_time')[:20]
    context = {
        "last_ten_posts": last_ten_posts,
        "last_ten_comments": last_ten_comments
    }
    return render(request, 'pages/feed.html', context)


# @login_required
def go_to_link(request, hashid):
    hashids = Hashids(salt='tarjimonlar')
    realid = hashids.decode(hashid)[0]
    url = 'https://fb.com/{objid}'.format(objid=realid)
    return HttpResponseRedirect(url)
