#coding: utf-8
'''
Created on 2013-1-1

@author: wolf_m
'''
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.forms.login import LoginForm
from doorfy_server.account.forms.register import RegisterForm

@csrf_protect
def home(request):
    '''
    首页view的显示
    '''
    if request.method == 'POST':    
        registerForm = RegisterForm(request.POST)
        return HttpResponse('Hello world!')
    else:
        registerForm = RegisterForm()
        loginForm = LoginForm()   
    c = {"registerForm":registerForm,"loginForm":loginForm}
    return render(request, "index.html", c)

def about(request):
    c = {}
    return render(request, "about.html", c, context_instance=RequestContext(request))

def contact(request):
    c = {}
    return render(request, "contact.html", c, context_instance=RequestContext(request))