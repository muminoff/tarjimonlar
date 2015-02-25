from django.shortcuts import render
from django.db.models import Count, Sum
from django.views.decorators.cache import cache_page
from core.models import Member, Post, Comment


def index_page(request):
    last_ten_posts = Post.objects.order_by('-created_time')[:10]
    last_ten_comments = Comment.objects.order_by('-created_time')[:10]

    context = {
        "next": request.GET.get('next'),
        "last_ten_posts": last_ten_posts,
        "last_ten_comments": last_ten_comments
    }
    return render(request, 'feed.html', context)


@cache_page(60 * 5)
def members_page(request):
    total_members = Member.objects.count()
    top_posters = Member.objects.annotate(num_posts=Count('post')).order_by('-num_posts')[:10]
    top_commentors = Member.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')[:10]
    top_liked_posters = Post.objects.annotate(creator_times=Count('creator__name', distinct=True)).order_by('-likes')[:10]
    top_liked_commentors = Comment.objects.annotate(creator_times=Count('creator__name', distinct=True)).order_by('-likes')[:10]

    context = {
        "total_members": total_members,
        "top_posters": top_posters,
        "top_commentors": top_commentors,
        "top_liked_posters": top_liked_posters,
        "top_liked_commentors": top_liked_commentors,
        "next": request.GET.get('next')
    }

    return render(request, 'pages/members.html', context)


@cache_page(60 * 5)
def posts_page(request):
    # qs = (Post.objects.all().
    #       extra(select={
    #           'day': 'extract(day from created_time)',
    #           'month': 'extract(month from created_time)',
    #           'year': 'extract(year from created_time)',
    #       }).
    #       values('month', 'year', 'day').
    #       annotate(count_posts=Count('created_time')))
    # qs = qs.order_by('created_time')
    # total = 0
    # json_values = []
    # for item in qs:
    #     total += item['count_posts']
    #     json_values.append(
    #         {
    #             'day': item['day'],
    #             'month': item['month'],
    #             'year': item['year'],
    #             'count_posts': total
    #         }
    #     )

    context = {
        "total_posts": Post.objects.count(),
        "top_liked_posts": Post.objects.order_by('-likes')[:10],
        "top_commented_posts": Post.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')[:10],
        # "jsondata": json_values,
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


def search_page(request):
    context = {
        "next": request.GET.get('next')
    }
    return render(request, 'pages/search.html', context)


def about_page(request):
    context = {"next": request.GET.get('next')}
    return render(request, 'pages/about.html', context)
