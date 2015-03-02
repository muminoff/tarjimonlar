#! -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _ 


def navbar(request):
    menus = OrderedDict([
        # ('index_page', {'title': 'Тасма', 'icon': 'article'}),
        ('members_page', {'title': 'Гуруҳ аъзолари', 'icon': 'user', 'submenu': False}),
        ('posts_page', {'title': 'Постлар', 'icon': 'post', 'submenu': False}),
        ('comments_page', {'title': 'Шарҳлар', 'icon': 'comment', 'submenu': False}),
        ('haystack_search', {'title': 'Қидирув', 'icon': 'search', 'submenu': False}),
        ('about_page', {'title': 'Лойиҳа ҳақида', 'icon': 'info', 'submenu': False}),
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
