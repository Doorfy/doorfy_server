# coding:utf-8
'''
Created on 2013-1-4

@author: wolf_m
'''
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.family.models import Family_User
from doorfy_server.util.logger import getLogger

LOG = getLogger()

@csrf_protect
def family_list(request): 
    if request.method == 'POST': 
        pass
    else:
        if request.user.is_authenticated():
            user = request.user
            familyUser = Family_User.objects.filter(user=user)
            c = {'familyUser':familyUser}
            return render(request, "family/list.html", c, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/")
