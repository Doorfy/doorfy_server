#coding:utf-8

'''
Created on Sep 13, 2012

@author: HP
'''

from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.account_util import user_required
from doorfy_server.account.forms.update_nickname import UpdateNicknameForm

@user_required
@csrf_protect
def updateNickname(request):
    user = request.user
    if request.method == 'POST':
        updateNicknameForm = UpdateNicknameForm(request.POST)
        c = {"updateNicknameForm":updateNicknameForm}
        if updateNicknameForm.is_valid():
            cd = updateNicknameForm.cleaned_data
            nickname = cd['nickname']
            up = user.get_profile()
            up.nickname=nickname
            up.save()
            c['successMessage'] = '昵称修改成功!'
        else:
            c['errorMessage'] = '请输入昵称!'
        return render(request, "account/settings.html", c, context_instance=RequestContext(request))
    else:
        pass
