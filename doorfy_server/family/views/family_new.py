#coding:utf-8
'''
Created on 2013-1-7

@author: wolf_m
'''
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def family_new(request):
    if request.method == 'POST': 
        pass
    else:
        if request.user.is_authenticated():
            c = {}
            return render(request, "family/new.html", c, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/")