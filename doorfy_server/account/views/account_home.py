#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.forms.login import LoginForm
from doorfy_server.account.forms.register import RegisterForm
from doorfy_server.settings import REGISTRATION_OPEN
from doorfy_server.util.handy import validateEmail
from doorfy_server.util.logger import getLogger


LOG = getLogger()

@csrf_protect
def accountHome(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'login':
            loginErrorMessage = ''
            loginCheck = True
            username = request.POST.get('username')
            password = request.POST.get('password')
            if len(username) == 0:
                loginErrorMessage = '请输入用户名!'
                loginCheck = False
            if loginCheck and len(password) == 0:
                loginErrorMessage = '请输入密码!'
                loginCheck = False
            if loginCheck and not validateEmail(username):
                loginErrorMessage = '请输入正确的email!'
            user = auth.authenticate(username=username, password=password) 
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                request.session['user'] = user
            else:
                loginErrorMessage = '用户名密码错误!'     
            return HttpResponse(loginErrorMessage)
        else:
            registerForm = RegisterForm(request.POST)
            if registerForm.is_valid():
                return HttpResponse('register false')
            return HttpResponse('register')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/door/list/') 
        if REGISTRATION_OPEN:
            registerForm = RegisterForm()
            loginForm = LoginForm()
            c = {'registerForm':registerForm, 'loginForm':loginForm}
            return render(request, "account/index.html", c, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/account/invitation/')
    