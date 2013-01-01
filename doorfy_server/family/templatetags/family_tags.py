#coding:utf-8
'''
Created on Sep 2, 2012

@author: HP
'''
from django import template
from doorfy_server.settings import DEBUG

register = template.Library()

@register.filter
def keyvalue(obj, key):    
    return obj[key]

@register.filter
def getCloudURL(cloudName):
    if DEBUG:
        return 'http://storage.aliyun.com/doorfy/test/' + cloudName
    else:
        return 'http://storage.aliyun.com/doorfy/' + cloudName

@register.filter
def getDoorTitle(door):
    try:
        if door != None:
            return door.name
    except:
        pass
    return '门扉'

