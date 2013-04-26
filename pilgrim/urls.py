# -*- coding: utf-8 -*-

from .utils import REGEX_JID, REGEX_HOSTNAME

from django.conf.urls import patterns, url

urlpatterns = patterns('pilgrim.views',
    url(r'^$', 'apiwrapper'),

    url(r'^minions/$', 'minions_list'),
    url(r'^minions/(?P<tgt>' + REGEX_HOSTNAME + ')/$', 'minions_details'),

    url(r'^jobs/$', 'jobs_list'),
	url(r'^jobs/(?P<jid>' + REGEX_JID + ')/$', 'jobs_details'),

    url(r'^ping/(?P<tgt>' + REGEX_HOSTNAME + ')/$', 'ping'),
    url(r'^sys/(?P<tgt>' + REGEX_HOSTNAME + ')/$', 'sys'),
    url(r'^echo/(?P<tgt>' + REGEX_HOSTNAME + ')/(?P<arg>\w+)/$', 'echo'),
    url(r'^install/(?P<tgt>' + REGEX_HOSTNAME + ')/(?P<arg>\w+)/$', 'pkg'),
    url(r'^run/(?P<tgt>' + REGEX_HOSTNAME + ')/(?P<arg>\w+)/$', 'run'),
    url(r'^sls/(?P<tgt>' + REGEX_HOSTNAME + ')/(?P<arg>\w+)/$', 'sls'),
    url(r'^keys/$', 'keys'),
)
