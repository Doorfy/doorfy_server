#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 1, 2012

@author: HP
'''

from django import forms

# Update Nick Name Form  
class UpdateNicknameForm(forms.Form):
    ''' 
    标准form写法，包括自定义属性，自定义文案，自定义校验规则。
    '''
    nickname = forms.CharField(required=True, widget=forms.TextInput(attrs={'size':'15','id':'nickname', 'tabindex':'1', 'placeholder':'新昵称', 'autocomplete':'off'}),
                               error_messages={
                                        'required' : "请输入昵称"
                                        })
    #自定义校验规则
    def clean_username(self):
        nickname = self.cleaned_data['nickname']
        return nickname
