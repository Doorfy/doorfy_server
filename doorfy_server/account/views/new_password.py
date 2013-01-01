#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.forms.login import LoginForm
from doorfy_server.account.forms.new_password import NewPasswordForm
from doorfy_server.util.logger import getLogger



LOG = getLogger()

@csrf_protect
def newPassword(request):
    if request.method == 'POST':
        try:
            form = NewPasswordForm(request.POST)
            key = request.POST['key']
            username = request.POST['username']
            if form.is_valid():
                user = User.objects.get(username=username)
                up = user.get_profile()
                try:
                    if up.password_key == key:                
                        user.set_password(request.POST['password1'])
                        user.save()
                        up.password_key = ''
                        up.save()
                        form = LoginForm()
                        infoMessage = '密码修改成功'
                        c = {'infoMessage':infoMessage}
                        return render(request, "account/active_info.html", c, context_instance=RequestContext(request))
                    else:
                        errorMessage = '非法修改密码'
                        c = {'form': form, 'username':username, 'key':key, 'errorMessage':errorMessage}
                        return render(request, "account/new_password.html", c, context_instance=RequestContext(request))
                    
                except User.DoesNotExist:
                    infoMessage = '您输入的邮箱系统不存在。'
                    return render_to_response("account/forgot_password.html", {"form":form, "infoMessage":infoMessage})                
            else:
                c = {'form': form, 'username':username, 'key':key}
                return render(request, "account/new_password.html", c, context_instance=RequestContext(request))
        except Exception as ex:
            LOG.error(__name__ + ':' + str(ex))
    else:
        LOG.warn('修改密码不允许使用get方法')