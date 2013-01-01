#coding:utf-8
'''
Created on Aug 20, 2012

@author: HP
'''
from django.forms.widgets import Input
import random
import socket

def getLocalIPAddress():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip


def validateEmail(email):
    '''
    验证 email 是否合法
    '''
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
    
class Html5EmailInput(Input): 
    '''
    html5的输入框
    '''
    input_type = 'email'
    
def getRandomPassword():
    source = '1234567890abcdefghijklmnopqrstuvwxyz'
    pwd = ''
    for i in range(6):
        pwd = pwd + source[random.randint(0, len(source) - 1)]
    return pwd

if __name__ == '__main__':
    pwd = getRandomPassword()
    print pwd
    
    
    
