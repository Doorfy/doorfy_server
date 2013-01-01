#coding: utf-8
'''
Created on Apr 22, 2012

@author: HP
'''

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.forms.widgets import Input
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from doorfy_server.settings import SITE_DOMAIN
from doorfy_server.util.logger import getLogger
from doorfy_server.util.mail import sendMail
import uuid



LOG = getLogger()

def sendForgotPasswordEmail(user):
    '''
    通过user对象发送忘记密码邮件
    '''
    try:
        up = user.get_profile()
        key = str(uuid.uuid4())
        up.password_key = key
        up.save()
        forgotPasswordLink = 'http://' + SITE_DOMAIN + '/account/active?u=' + user.username + '&pk=' + str(key)
        LOG.debug('Forgot password link:' + forgotPasswordLink)
        content = '<p>' + user.email + '，你好：</p><p>您的修改密码链接如下：</p><p><a href="' + forgotPasswordLink + '">' + forgotPasswordLink + '</a></p><p>如果链接不可用，请复制链接到浏览器的地址栏，然后直接访问。如果您没有点击过忘记密码链接，请无视此邮件。</p><p>谢谢！</p>'
        sendMail('密码找回邮件', content, user.email)
    except Exception as e:
        LOG.error('Send Email Error:' + str(e))

def user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = userPassesTestWith403(
        lambda u: needUser(u),
        login_url=login_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def needUser(user):
    if user.is_authenticated():
        return True
    return False

def userPassesTestWith403(test_func, login_url=None):
    """
    Decorator for views that checks that the user passes the given test.
    
    Anonymous users will be redirected to login_url, while users that fail
    the test will be given a 403 error.
    """
    if not login_url:
        from django.conf import settings
        login_url = settings.LOGIN_URL
    def _dec(view_func):
        def _checklogin(request, *args, **kwargs):
            if not request.user.is_authenticated():
                return HttpResponseRedirect('%s?%s=%s' % (login_url, REDIRECT_FIELD_NAME, request.get_full_path()))
            elif test_func(request.user):
                return view_func(request, *args, **kwargs)
            else:
                resp = render_to_response('account/403.html', context_instance=RequestContext(request))
                resp.status_code = 403
                return resp
        _checklogin.__doc__ = view_func.__doc__
        _checklogin.__dict__ = view_func.__dict__
        return _checklogin
    return _dec

def sendActiveEmail(user):
    '''
    通过user对象发送激活邮件
    '''
    try:
        key = user.get_profile().active_key
        activeLink = 'http://' + SITE_DOMAIN + '/account/active?u=' + user.username + '&ak=' + str(key)
        LOG.debug('Active link:' + activeLink)
        content = '<p>你好：</p><p>您的激活链接如下：</p><p><a href="' + activeLink + '">' + activeLink + '</a></p><p>如果激活链接不可用，请复制链接到浏览器的地址栏，然后直接访问。</p><p>谢谢！</p>'
        sendMail('激活邮件', content, user.email)
    except Exception as e:
        LOG.error('Send Email Error:' + str(e))
        
