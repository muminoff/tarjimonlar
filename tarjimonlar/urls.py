# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^$', 'core.views.index_page', name='index_page'),
    url(r'^statistics/', 'core.views.gen_stat_page', name='gen_stat_page'),
    url(r'^about/', 'core.views.about_page', name='about_page'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
