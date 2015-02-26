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
    url(r'^members/', 'core.views.members_page', name='members_page'),
    url(r'^posts/', 'core.views.posts_page', name='posts_page'),
    url(r'^comments/', 'core.views.comments_page', name='comments_page'),
    # url(r'^find/', 'core.views.search_page', name='search_page'),
    url(r'^about/', 'core.views.about_page', name='about_page'),
    url(r'^search/', include('haystack.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
