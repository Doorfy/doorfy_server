#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.contrib import auth
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.forms.login import LoginForm
from doorfy_server.util.logger import getLogger


LOG = getLogger()

@csrf_protect
def login(request): 
    '''
    登陆逻辑
    '''
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        nextURL = request.POST.get('next', None)
        if loginForm.is_valid():
            cd = loginForm.cleaned_data
            username = cd['username']
            password = cd['password']
            
            user = auth.authenticate(username=username, password=password)             
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                if not request.POST.get('login-remember', None):
                    request.session.set_expiry(0)
                c = {"url":''}
                # Redirect to a success page.            
                if nextURL:
                    c['url'] = nextURL
                    return render(request, "account/login_success.html", c,context_instance=RequestContext(request))    
                return render(request, "account/login_success.html", c,context_instance=RequestContext(request))          
            else:
                # Show an error page
                loginErrorMessage = '密码错误请重试。'
                c = {"loginForm":loginForm, "loginErrorMessage":loginErrorMessage, "next":nextURL}
                return render(request, "account/login.html", c, context_instance=RequestContext(request))
        else:
            c = {"loginForm":loginForm, "next":nextURL}
            return render(request, "account/login.html", c, context_instance=RequestContext(request))
    else:
        loginForm = LoginForm()
        loginErrorMessage = ''
        loginInfoMessage = ''
        c = {'loginForm':loginForm, "loginErrorMessage":loginErrorMessage, "loginInfoMessage":loginInfoMessage, "next":"/door/list/"}
        return render(request, "account/login.html", c, context_instance=RequestContext(request))
