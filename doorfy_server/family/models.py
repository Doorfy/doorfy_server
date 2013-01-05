# coding:utf-8
'''
Created on 2013-1-5

@author: wolf_m
'''
from django.contrib.auth.models import User
from django.db import models

class Family(models.Model):
    # This field is required.
    name = models.CharField(max_length=100, db_index=True)      # 家庭名称
    creator = models.ForeignKey(User)                           # 家庭建立者
    insert_datetime = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)    # 家庭建立时间
    modify_datetime = models.DateTimeField(auto_now=True, auto_now_add=True, blank=True, null=True)     # 家庭修改时间
    privilige_type = models.SmallIntegerField(default=0)    # 权限设置 保留字段
    business_type = models.SmallIntegerField(default=0)     # 类型设置 保留字段
    desc = models.TextField()                       # 家庭描述
    status = models.SmallIntegerField(default=0)    # 状态 -1为删除       
    class Meta:
        # 自定义表名   
        db_table = 'family'

class Family_User(models.Model):
    '''
   家庭成员表
    '''
    family = models.ForeignKey(Family)  # 家庭
    user = models.ForeignKey(User)  # 人员
    type = models.SmallIntegerField(default=0)  # 保留字段
    class Meta:
        # 自定义表名   
        db_table = 'family_user'
        
class Attach(models.Model):
    '''
    附件表
    '''
    name = models.CharField(max_length=100, db_index=True)  # 附件名称
    cloud_name = models.CharField(max_length=255)  # 附件云端名称
    creator = models.ForeignKey(User)  # 上传人
    insert_datetime = models.DateTimeField(blank=True, null=True)  # 上传时间
    datetime = models.DateTimeField(blank=True, null=True)  # 附件标识时间
    longitude = models.FloatField(blank=True, null=True)  # 附件纬度
    latidude = models.FloatField(blank=True, null=True)  # 附件经度
    media_type = models.CharField(max_length=128)  # 附件类型  1:图片;
    abuse_count = models.IntegerField(default=0)  # 举报次数
    status = models.SmallIntegerField(default=0)  # 状态 -1为删除
    class Meta:
        # 自定义表名   
        db_table = 'attach'
        
class Attach_Family(models.Model):
    '''
   家庭成员表
    '''
    family = models.ForeignKey(Family)  # 家庭
    attach = models.ForeignKey(Attach)  # 附件
    class Meta:
        # 自定义表名   
        db_table = 'attach_family'
        
class Family_Comment(models.Model):
    '''
    家庭留言表
    '''
    family = models.ForeignKey(Family)  # 活动
    creator = models.ForeignKey(User)  # 评论发布人
    insert_datetime = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)  # 上传时间
    modify_datetime = models.DateTimeField(auto_now=True, auto_now_add=True, blank=True, null=True)  # 修改
    content = models.SmallIntegerField(default=0)  # 评论内容
    abuse_count = models.SmallIntegerField(default=0)  # 举报次数
    status = models.SmallIntegerField(default=0)  # 状态 -1为删除
    class Meta:
        # 自定义表名   
        db_table = 'family_comment'

class Attach_Comment(models.Model):
    '''
    附件对应的评论
    '''
    attach = models.ForeignKey(Attach)  # 附件
    creator = models.ForeignKey(User)  # 评论发布人
    insert_datetime = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)  # 上传时间
    modify_datetime = models.DateTimeField(auto_now=True, auto_now_add=True, blank=True, null=True)  # 修改时间
    content = models.TextField()  # 评论内容
    abuse_count = models.SmallIntegerField(default=0)  # 举报次数
    status = models.SmallIntegerField(default=0)  # 状态 -1为删除
    class Meta:
        # 自定义表名   
        db_table = 'attach_comment'
