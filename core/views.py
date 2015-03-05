from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db.models import Count, Sum
from django.views.decorators.cache import cache_page, never_cache
from core.models import Member, Post, Comment
from itertools import chain
from random import sample
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from hashids import Hashids


@never_cache
def index_page(request):
    top_15_posters = Member.objects.annotate(
            num_posts=Count('post')).order_by('-num_posts')[:50]
    top_15_commentors = Member.objects.annotate(
            num_comments=Count('comment')).order_by('-num_comments')[:50]

    context = {
        "hall_of_fame": sample(
            list(chain(top_15_posters, top_15_commentors)), 100),
    }
    return render(request, 'home.html', context)


@cache_page(60 * 5)
def facts_page(request):
    total_members = Member.objects.count()
    top_posters = Member.objects.annotate(
            num_posts=Count('post')).order_by('-num_posts')[:10]
    top_commentors = Member.objects.annotate(
            num_comments=Count('comment')).order_by('-num_comments')[:10]
    top_liked_posters = Post.objects.annotate(
            creator_times=Count('creator__name', distinct=True)).order_by('-likes')[:10]
    top_liked_commentors = Comment.objects.annotate(
            creator_times=Count('creator__name', distinct=True)).order_by('-likes')[:10]
    top_commented_posts = Post.objects.annotate(
            num_comments=Count('comment')).order_by('-num_comments')[:10]
    top_liked_posts = Post.objects.order_by('-likes')[:10]

    context = {
        "total_members": total_members,
        "top_posters": top_posters,
        "top_commentors": top_commentors,
        "top_liked_posters": top_liked_posters,
        "top_liked_commentors": top_liked_commentors,
        "top_commented_posts": top_commented_posts,
        "top_liked_posts": top_liked_posts,
        "next": request.GET.get('next')
    }

    return render(request, 'pages/facts.html', context)


@cache_page(60 * 5)
def posts_page(request):

    context = {
        "total_posts": Post.objects.count(),
        "next": request.GET.get('next')
    }
    return render(request, 'pages/posts.html', context)


@cache_page(60 * 5)
def comments_page(request):

    context = {
        "total_comments": Comment.objects.count(),
        "next": request.GET.get('next')
    }
    return render(request, 'pages/comments.html', context)

class TarjimonSearchView(SearchView):
    
    def get_context_data(self, *args, **kwargs):
        context = super(TarjimonSearchView, self).get_context_data(*args, **kwargs)
        return context


def about_page(request):
    context = {"next": request.GET.get('next')}
    return render(request, 'pages/about.html', context)

def go_to_link(request, hashid):
    hashids = Hashids(salt=settings.SECRET_KEY)
    realid = hashids.decode(hashid)[0]
    print realid
    url = 'https://fb.com/{objid}'.format(objid=realid)
    return HttpResponseRedirect(url)
