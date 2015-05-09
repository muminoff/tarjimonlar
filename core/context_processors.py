#! -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _ 


def navbar(request):
    menus = OrderedDict([
        ('feed_page', {'title': 'Сўнгги янгиликлар', 'icon': 'article', 'submenu': False}),
        ('stats_page', {'title': 'Умумий статистика', 'icon': 'stat', 'submenu': False}),
        ('members_page', {'title': 'Иштирокчилар', 'icon': 'user', 'submenu': False}),
        ('posts_page', {'title': 'Постлар', 'icon': 'post', 'submenu': False}),
        ('comments_page', {'title': 'Шарҳлар', 'icon': 'comment', 'submenu': False}),
        ('search_page', {'title': 'Қидирув', 'icon': 'search', 'submenu': False}),
        ('about_page', {'title': 'Лойиҳа ҳақида', 'icon': 'info', 'submenu': False}),
        ('subscribe_page', {'title': 'Обуна', 'icon': 'broadcast', 'submenu': False}),
        ])

    try: 
        name = resolve(request.path).url_name
        if name in menus:
            menus[name]['active'] = True 
    except:
        pass

    return {
            'menus': menus,
            }
