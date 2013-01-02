#coding:utf-8
'''
Created on Jan 1, 2013

@author: HP
'''
from django import forms
from doorfy_server.util.handy import Html5EmailInput

class InviteForm(forms.Form):
    ''' 
    标准form写法，包括自定义属性，自定义文案，自定义校验规则。
    '''
    username = forms.CharField(required=True, widget=Html5EmailInput(attrs={'size':'15','id':'invite-email', 'tabindex':'1', 'class':'invite-input', 'placeholder':'电子邮箱', 'autocomplete':'off'}),
                               error_messages={
                                        'required' : "请输入邮箱",
                                        'invalid'  : "请输入合法的电子邮箱。"})
    #自定义校验规则
    def clean_username(self):
        username = self.cleaned_data['username']
        return username