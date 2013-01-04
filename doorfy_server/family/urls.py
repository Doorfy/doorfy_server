#coding:utf-8
'''
Created on 2013-1-4

@author: wolf_m
'''
from django.conf.urls import patterns, url
from doorfy_server.family.views.family_list import family_list

urlpatterns = patterns('',
    #url(r'^$', accountHome),
    url(r'^list/(?P<userId>\d+)/$', family_list),
)