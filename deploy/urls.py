# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from core.views import TarjimonSearchView
from haystack.query import SearchQuerySet

from django.contrib import admin
admin.autodiscover()

qs = SearchQuerySet().order_by('-created_time', '-likes')

urlpatterns = patterns('',
    url(r'^login/$', 'core.views.login_page', name='login_page'),
    url(r'^facts/$', 'core.views.facts_page', name='facts_page'),
    url(r'^posts/$', 'core.views.posts_page', name='posts_page'),
    url(r'^comments/$', 'core.views.comments_page', name='comments_page'),
    url(r'^search/$', TarjimonSearchView(searchqueryset=qs, template='pages/search.html'), name='search_page'),
    url(r'^about/$', 'core.views.about_page', name='about_page'),
    url(r'^member-link/(?P<hashid>.+)$', 'core.views.go_to_link', name='go_to_link'),
    # User management
    url(r'^members/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + patterns('',
        url(r'^admin/', include(admin.site.urls)),
        )
