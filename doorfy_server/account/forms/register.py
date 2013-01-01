#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Mar 1, 2012

@author: HP
'''
#RegisterForm

from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.models import User
from doorfy_server.util.handy import Html5EmailInput


class RegisterForm(forms.Form):
    username = forms.EmailField(required=True, widget=Html5EmailInput(attrs={'size':'15','id':'register-username','tabindex':'1', 'class':'register-input', 'placeholder':'电子邮箱', 'autocomplete':'off'}),
                               error_messages={
                                        'required' : "请输入电子邮箱",
                                        'invalid'  : "请输入合法的电子邮箱"})
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'size':'15', 'id':'register-password1','tabindex':'2','class':'register-input','placeholder':'创建密码'}),error_messages={
                                        'required' : "请输入密码",
                                        'invalid'  : "请输入合法的密码"})
    captcha = CaptchaField(error_messages={
                                        'required' : "请输入验证码",
                                        'invalid'  : "请输入正确的验证码"})
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("用户名已存在")
        
