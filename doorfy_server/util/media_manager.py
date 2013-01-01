#coding:utf-8
'''
Created on May 1, 2012

@author: HP
'''

from doorfy_server.settings import DEBUG, CLOUD_HOST, CLOUD_ACCESS_ID, \
    CLOUD_SECRET_ACCESS_KEY, CLOUD_BUCKET
from doorfy_server.util.logger import getLogger
from doorfy_server.util.oss.oss_api import OssAPI
import os
import uuid



LOG = getLogger()

def addMedia(imgName, cloudObjectName):
    '''
    上传媒体文件到云服务器
    '''
    oss = OssAPI(CLOUD_HOST, CLOUD_ACCESS_ID, CLOUD_SECRET_ACCESS_KEY)
    tempPath = os.path.realpath(os.path.dirname(__file__))
    filename = os.path.join(tempPath, imgName)
    content_type = "image/jpeg"
    headers = {}
    fp = open(filename, 'rb')
    if DEBUG:
        res = oss.put_object_from_fp(CLOUD_BUCKET, 'test/' + cloudObjectName, fp, content_type, headers)
    else:
        res = oss.put_object_from_fp(CLOUD_BUCKET, cloudObjectName, fp, content_type, headers)
    fp.close()
    if (res.status / 100) == 2:
        LOG.info("put_object_from_fp OK")
    else:
        LOG.error("put_object_from_fp ERROR")  

def delMedia(cloudObjectName):
    '''
    根据云端名称删除云上的文件
    '''
    oss = OssAPI(CLOUD_HOST, CLOUD_ACCESS_ID, CLOUD_SECRET_ACCESS_KEY)
    headers = {}
    res = oss.delete_object(CLOUD_BUCKET, cloudObjectName, headers)
    if (res.status / 100) == 2:
        LOG.info("delete_object OK")
    else:
        LOG.error("delete_object ERROR")

if __name__ == '__main__':
    addMedia('yuicompressor-2.4.7.jar', 'test/' + str(uuid.uuid4()) + '.jar')   
    pass
    
