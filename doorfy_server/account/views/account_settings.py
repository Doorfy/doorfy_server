#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.account_util import user_required
from doorfy_server.account.forms.update_nickname import UpdateNicknameForm
from doorfy_server.util.sidebar_util import PAGE_NAME_DOOR_ACCOUNT_SETTINGS



@user_required
@csrf_protect
def accountSettings(request):
    if request.method == 'POST':
        pass
    else:
        updateNicknameForm = UpdateNicknameForm()
        c = {'pageName':PAGE_NAME_DOOR_ACCOUNT_SETTINGS, 'updateNicknameForm':updateNicknameForm}
        return render(request, "account/settings.html", c, context_instance=RequestContext(request))
