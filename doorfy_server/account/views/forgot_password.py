#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.account_util import sendForgotPasswordEmail
from doorfy_server.account.forms.forgot_password import ForgotPasswordForm
from doorfy_server.util.logger import getLogger

LOG = getLogger()

@csrf_protect
def forgotPassword(request): 
    '''
    忘记密码视图处理
    ''' 
    if request.method == 'POST':
        try:
            forgotPasswordForm = ForgotPasswordForm(request.POST)
            infoMessage = ''
            errorMessage = ''
            c = {}
            if forgotPasswordForm.is_valid():
                # username 为邮箱
                username = request.POST['username']
                try:
                    user = User.objects.get(username=username)
                    if user.is_active:
                        #重新发送忘记密码邮件
                        sendForgotPasswordEmail(user)
                        infoMessage = '已经发送忘记密码邮件到指定邮箱。'
                        c['infoMessage'] = infoMessage
                    else:
                        #未激活的用户不能发送忘记密码邮件
                        errorMessage = '此用户尚未激活，不能修改密码'
                        c['errorMessage'] = errorMessage 
                    return render(request, "account/active_info.html", c, context_instance=RequestContext(request))
                except User.DoesNotExist:
                    infoMessage = '您输入的邮箱系统不存在。'
                    c = {"forgotPasswordForm":forgotPasswordForm, "infoMessage":infoMessage}
                    return render(request, "account/forgot_password.html", c, context_instance=RequestContext(request))
            else:
                c = {"forgotPasswordForm":forgotPasswordForm, "infoMessage":infoMessage}
                return render(request, "account/forgot_password.html", c, context_instance=RequestContext(request))
        except Exception as ex:
            LOG.error(__name__ + ':' + str(ex))
    else:
        forgotPasswordForm = ForgotPasswordForm()
        errorMessage = ''
        infoMessage = ''
        c = {"forgotPasswordForm":forgotPasswordForm, "infoMessage":infoMessage, 'errorMessage':errorMessage}
        return render(request, "account/forgot_password.html", c)