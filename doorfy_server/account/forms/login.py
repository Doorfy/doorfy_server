#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 1, 2012

@author: HP
'''

from django import forms
from doorfy_server.util.handy import Html5EmailInput

# Login Form   
class LoginForm(forms.Form):
    ''' 
    标准form写法，包括自定义属性，自定义文案，自定义校验规则。
    '''
    username = forms.EmailField(required=True, widget=Html5EmailInput(attrs={'size':'15', 'id':'login-username','class':'login-input','autocomplete':'off','placeholder':'电子邮箱'}),
                               error_messages={
                                        'required' : "请输入邮箱",
                                        'invalid'  : "请输入合法的电子邮箱"})
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'size':'15', 'id':'login-password','class':'login-input','placeholder':'密码'}),
                               error_messages={
                                        'required' : "请输入密码",
                                        'invalid'  : "请输入合法的密码"})
    #自定义校验规则
    def clean_username(self):
        username = self.cleaned_data['username']
        return username
