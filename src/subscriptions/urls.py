# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from route import route


urlpatterns =    patterns('subscriptions.views',
       route(r'^$', GET='new', POST='create', name='subscribe'),
       url(r'^(\d+)/sucesso/$','success',name='success'),
)
