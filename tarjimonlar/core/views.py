from django.shortcuts import render
from django.db.models import Count
from core.models import Member, Post, Comment


def index_page(request):
    context = {"next": request.GET.get('next')}
    return render(request, 'base.html', context)


def members_page(request):
    top_posters = Member.objects.annotate(num_posts=Count('post')).order_by('-num_posts')[:10]
    top_commentors = Member.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')[:10]
    context = {
        "top_posters": top_posters,
        "top_commentors": top_commentors,
        "total_members": Member.objects.count(),
        "total_admins": Member.objects.filter(admin=True).count(),
        "all_admins": Member.objects.filter(admin=True),
        "next": request.GET.get('next')
    }
    return render(request, 'pages/members.html', context)


def posts_page(request):
    qs = (Post.objects.all().
          extra(select={
              'month': 'extract(month from created_time)',
              'year': 'extract(year from created_time)',
          }).
          values('month', 'year').
          annotate(count_posts=Count('created_time')))
    qs = qs.order_by('created_time')
    total = 0
    json_values = []
    for item in qs:
        total += item['count_posts']
        json_values.append(
            {
                'month': item['month'],
                'year': item['year'],
                'count_posts': total
            }
        )

    context = {
        "total_posts": Post.objects.count(),
        "jsondata": json_values,
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
