# coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

    
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.forms.register import RegisterForm
from doorfy_server.account.models import UserProfile
from doorfy_server.util.logger import getLogger
import json



LOG = getLogger()

@csrf_protect
def register(request): 
    '''
    用户注册逻辑
    '''
    REGISTER_OK = 1
    REGISTER_USER_EXIST = -1
    REGISTER_USERNAME_ERROR = -2
    REGISTER_PASSWORD_ERROR = -3
    
    result = {'infoMessage':'', 'errorMessag':'', 'code':[]}
    if request.method == 'POST':    
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = request.POST['username']
            try:
                User.objects.get(username=username)                      
                result['infoMessage'] = '用户名已存在'
                result['code'].append(REGISTER_USER_EXIST)
            except User.DoesNotExist:
                u = User.objects.create_user(username, username, request.POST['password1'])
                u.is_active = True
                u.save()             
                up = UserProfile(user=u)
                up.password_key = ''
                up.save()
                #sendActiveEmail(u)
                result['code'].append(REGISTER_OK)
                result['userId'] = u.id 
                user = auth.authenticate(username=username, password=request.POST['password1'])
                auth.login(request, user)
            return HttpResponse(json.dumps(result))
        else:
            if registerForm.errors['username']:
                result['code'].append(REGISTER_USERNAME_ERROR)
            if registerForm.errors['password1']:
                result['code'].append(REGISTER_PASSWORD_ERROR)
            return HttpResponse(json.dumps(result))
    else:
        pass

