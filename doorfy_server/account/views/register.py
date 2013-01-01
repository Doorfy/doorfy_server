#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.account_util import sendActiveEmail
from doorfy_server.account.forms.register import RegisterForm
from doorfy_server.account.models import UserProfile
from doorfy_server.util.logger import getLogger
import uuid


LOG = getLogger()


@csrf_protect
def register(request): 
    '''
    用户注册逻辑
    '''
    infoMessage = ''
    errorMessage = ''
    if request.method == 'POST':    
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = request.POST['username']
            try:
                User.objects.get(username=username)                      
                infoMessage = '用户名已存在'
            except User.DoesNotExist:
                u = User.objects.create_user(username, username, request.POST['password1'])
                u.is_active = False
                u.save()             
                up = UserProfile(user=u)
                up.active_key = str(uuid.uuid4())
                up.password_key = ''
                up.save()
                sendActiveEmail(u)
                infoMessage = '已经发送激活邮件到指定邮箱，请及时激活帐号登陆系统。'
            # TODO 注册成功以后跳转到用户门首页
            c = {}
            return render(request, "account/register_success.html", c, context_instance=RequestContext(request))
        else:
            c = {"registerForm":registerForm, "infoMessage":infoMessage, 'errorMessage':errorMessage}
            return render(request, "account/register.html", c, context_instance=RequestContext(request))
    else:
        registerForm = RegisterForm()
        registerErrorMessage = ''
        registerInfoMessage = ''
        c = {'registerForm':registerForm, "registerErrorMessage":registerErrorMessage, "registerInfoMessage":registerInfoMessage}
        return render(request, "account/register.html", c, context_instance=RequestContext(request))

