# coding:utf-8
'''
Created on 2013-1-8

@author: wolf_m
'''
from django import forms


class CreatFamilyForm(forms.Form):
    ''' 
    标准form写法，包括自定义属性，自定义文案，自定义校验规则。
    '''
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'size':'15', 'id':'name', 'class':'login-input', 'autocomplete':'off', 'placeholder':'名称'}),
                               error_messages={
                                        'required' : "请输入用户名",
                                        'invalid'  : "请输入合法的用户名"})
    desc = forms.CharField(required=True, widget=forms.TextInput(attrs={'size':'15', 'id':'desc', 'class':'login-input', 'placeholder':'描述'}),
                               error_messages={
                                        'required' : "请输入家庭描述",
                                        'invalid'  : "请输入合法的家庭描述"})
    # 自定义校验规则
    def clean_name(self):
        username = self.cleaned_data['name']
        return username
