#coding:utf-8
'''
Created on Sep 12, 2012

@author: HP
'''

from django.http import HttpResponse
from doorfy_server.account.account_util import user_required, \
    sendForgotPasswordEmail
import json


@user_required
def resetPassword(request):
    if request.method == 'POST':
        pass
    else:
        user = request.user
        sendForgotPasswordEmail(user)
        result = {'r':1}
        return HttpResponse(json.dumps(result))
