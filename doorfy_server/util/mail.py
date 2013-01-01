#coding:utf-8
'''
Created on Feb 29, 2012

@author: HP
'''
from django.core.mail.message import EmailMessage
from doorfy_server.settings import DEBUG_EMAIL
from doorfy_server.util.logger import getLogger



LOG = getLogger()

def sendMail(subject, content, to):
    '''
    发送邮件
    '''   
    if len(DEBUG_EMAIL) != 0:
        to = DEBUG_EMAIL
    msg = EmailMessage(subject, content, None, [to])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    LOG.debug('[Send Mail]Subject:' + subject + '; To: ' + to + '; Content: ' + content)
