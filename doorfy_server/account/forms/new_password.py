#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Mar 1, 2012

@author: HP
'''
#RegisterForm
from django import forms
from django.contrib.auth.models import User
class NewPasswordForm(forms.Form):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'size':'30', 'class':'new-password-input', 'placeholder':'新密码', }),
                                error_messages={
                                        'required' : "请输入密码."})
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'size':'30', 'class':'new-password-input', 'placeholder':'新密码确认', }),
        help_text="Enter the same password as above, for verification.",
        error_messages={
                                        'required' : "请输入确认密码."})
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("A user with that username already exists.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("两次密码不一致.")
        return password2
        
