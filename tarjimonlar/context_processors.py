#! -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _ 


def navbar(request):
    menus = OrderedDict([
        ('members_page', {'title': 'Иштирокчилар', 'icon': 'user'}),
        ('posts_page', {'title': 'Постлар', 'icon': 'post'}),
        ('comments_page', {'title': 'Комментлар', 'icon': 'comment'}),
        ('search_page', {'title': 'Қидирув', 'icon': 'search'}),
        ('about_page', {'title': 'Лойиҳа ҳақида', 'icon': 'info'}),
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
