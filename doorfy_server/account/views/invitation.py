#coding: utf-8
'''
Created on Jan 1, 2013

@author: HP
'''
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from doorfy_server.account.forms.invite import InviteForm
from doorfy_server.account.models import Invitation
from doorfy_server.settings import SECRET_KEY, SITE_DOMAIN
from doorfy_server.util.logger import getLogger
import hashlib
import json

LOG = getLogger()

@csrf_protect
def invitation(request):
    ALREADY_INVITED = -1
    EMAIL_ERROR = -2
    INVITATION_OK = 1
    if request.method == 'POST':
        inviteForm = InviteForm(request.POST)
        result = {}
        if inviteForm.is_valid():
            email = request.POST['username']
            if(len(Invitation.objects.filter(email=email)) == 0):
                result['code'] = INVITATION_OK
                # 生成邀请链接
                key = hashlib.md5(SECRET_KEY + email).hexdigest()
                url = 'http://' + SITE_DOMAIN + '/account/invitation/?key=' + key + '&mail=' + email
                invitation = Invitation(email=email, invited=False)
                invitation.save()
            else:
                result['code'] = ALREADY_INVITED
            return HttpResponse(json.dumps(result))
        else:
            result['code'] = EMAIL_ERROR
            return HttpResponse(json.dumps(result))
    else:
        if request.GET['key'] != None:
            pass
        form = InviteForm()
        c = {'inviteForm': form}
        return render(request, "account/invite.html", c, context_instance=RequestContext(request))
