#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.forms.login import LoginForm
from doorfy_server.util.logger import getLogger
import json


LOG = getLogger()

@csrf_protect
def login(request): 
    '''
    登陆逻辑
    '''
    LOGIN_OK = 1
    LOGIN_PASSWORD_NO_CORRECT = -1
    LOGIN_USERNAME_ERROR = -2
    LOGINREGISTER_PASSWORD_ERROR = -3
    result = {'infoMessage':'', 'errorMessag':'', 'code':[]}
    if request.method == 'POST':  
        loginForm = LoginForm(request.POST)
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
                result['code'].append(LOGIN_OK)
                result['userId'] = user.id
                return HttpResponse(json.dumps(result))          
            else:
                result['code'].append(LOGIN_PASSWORD_NO_CORRECT)
                return HttpResponse(json.dumps(result))
        else:
            if loginForm.errors['username']:
                result['code'].append(LOGIN_USERNAME_ERROR)
            if loginForm.errors['password']:
                result['code'].append(LOGINREGISTER_PASSWORD_ERROR)
            return HttpResponse(json.dumps(result))
    else:
        pass
