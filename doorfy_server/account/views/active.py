#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from doorfy_server.account.forms.forgot_password import ForgotPasswordForm
from doorfy_server.account.forms.new_password import NewPasswordForm
from doorfy_server.util.logger import getLogger


LOG = getLogger()

def active(request):
    '''
    激活帐号逻辑及忘记密码逻辑
    '''
    if request.method == 'POST':
        LOG.warn('激活链接不能使用POST方法')
    else:
        username = request.GET['u']
        # 账户激活key
        userActiveKey = request.GET.get('ak' or None)
        # 忘记密码key
        userPasswordKey = request.GET.get('pk' or None)
        
        c = {}
        try:
            #发送了激活邮件的用户肯定在auth_user表中有纪录。
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            if userActiveKey:
                errorMessage = '帐户激活失败!请仔细核对激活邮件URL！' 
            else:
                errorMessage = '修改密码失败!请仔细核对修改密码邮件URL！'
            c['errorMessage'] = errorMessage
            return render(request, "account/active_info.html", c, context_instance=RequestContext(request)) 
        up = user.get_profile()
        activeDBKey = up.active_key
        passwordDBKey = up.password_key
        errorMessage = ''
        infoMessage = ''
        if userActiveKey:
            #用户激活
            if len(activeDBKey) == 0:
                errorMessage = '此帐号已经被激活！'
                c['errorMessage'] = errorMessage                  
            elif userActiveKey == activeDBKey:
                up.active_key = ''
                user.is_active = True;
                user.save()
                up.save()
                infoMessage = '帐号激活成功！'
                c['infoMessage'] = infoMessage 
            else:
                errorMessage = '帐户激活失败!请仔细核对激活邮件URL！'           
                c['errorMessage'] = errorMessage
            return render(request, "account/active_info.html", c, context_instance=RequestContext(request))   
        else:
            #忘记密码
            if len(passwordDBKey) == 0:
                form = ForgotPasswordForm()
                infoMessage = '此帐号不能修改密码'
                return HttpResponse(infoMessage)                 
            elif userPasswordKey == passwordDBKey:
                form = NewPasswordForm()
                c = {'form': form, 'username':user.username, 'key':userPasswordKey}
                return render(request, "account/new_password.html", c, context_instance=RequestContext(request))       
            else:
                form = ForgotPasswordForm()
                errorMessage = '帐户修改密码失败!请仔细核对修改密码邮件URL！'           
                infoMessage = ''
                c['errorMessage'] = errorMessage
                return render(request, "account/active_info.html", c, context_instance=RequestContext(request)) 