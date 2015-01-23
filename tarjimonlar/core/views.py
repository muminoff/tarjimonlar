from django.shortcuts import render


def index_page(request):
    context = {"next": request.GET.get('next')}
    return render(request, 'base.html', context)


def gen_stat_page(request):
    context = {"next": request.GET.get('next')}
    return render(request, 'pages/gen_stat.html', context)
