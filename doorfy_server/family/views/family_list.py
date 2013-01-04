#coding:utf-8
'''
Created on 2013-1-4

@author: wolf_m
'''
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.util.logger import getLogger

LOG = getLogger()

@csrf_protect
def family_list(request,userId): 
    if request.method == 'POST': 
        pass
    else:
        c = {}
        return render(request, "family/list.html", c, context_instance=RequestContext(request))