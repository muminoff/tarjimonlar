from django.shortcuts import render
from core.models import Member, Post, Comment


def index_page(request):
    context = {"next": request.GET.get('next')}
    return render(request, 'base.html', context)


def members_page(request):
    context = {
        "total_members": Member.objects.count(),
        "total_admins": Member.objects.filter(admin=True).count(),
        "next": request.GET.get('next')
    }
    return render(request, 'pages/members.html', context)


def posts_page(request):
    context = {
        "total_posts": Post.objects.count(),
        "next": request.GET.get('next')
    }
    return render(request, 'pages/posts.html', context)


def comments_page(request):
    context = {
        "total_comments": Comment.objects.count(),
        "next": request.GET.get('next')
    }
    return render(request, 'pages/comments.html', context)


def search_page(request):
    context = {
        "next": request.GET.get('next')
    }
    return render(request, 'pages/search.html', context)


def gen_stat_page(request):
    context = {"next": request.GET.get('next')}
    return render(request, 'pages/gen_stat.html', context)


def about_page(request):
    context = {"next": request.GET.get('next')}
    return render(request, 'pages/about.html', context)
