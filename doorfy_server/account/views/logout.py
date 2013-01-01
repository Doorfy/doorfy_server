#coding:utf-8
'''
Created on Sep 10, 2012

@author: HP
'''

from django.contrib import auth
from django.http import HttpResponseRedirect


def logout(request):
    '''
    用户注销
    '''
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")