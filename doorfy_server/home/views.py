#coding: utf-8
'''
Created on 2013-1-1

@author: wolf_m
'''
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.forms.invite import InviteForm
from doorfy_server.account.forms.login import LoginForm

@csrf_protect
def home(request):
    '''
    首页view的显示
    '''
    if request.method == 'POST':    
        return HttpResponse('Hello world!')
    else:
        loginForm = LoginForm() 
        inviteForm = InviteForm()  
    c = {"loginForm":loginForm, "inviteForm":inviteForm}
    return render(request, "index.html", c)

def about(request):
    c = {}
    return render(request, "about.html", c, context_instance=RequestContext(request))

def contact(request):
    c = {}
    return render(request, "contact.html", c, context_instance=RequestContext(request))
