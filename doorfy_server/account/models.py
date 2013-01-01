#coding: utf-8
from django.contrib.auth.models import User
from django.db import models

PERMISSION_ADMIN = 1
PERMISSION_LEADER = 2
PERMISSION_USER = 3

# Create your models here.
class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=128)         # 用户昵称
    permission = models.SmallIntegerField(default=0)
    active_key = models.CharField(max_length=128)       # 激活码
    password_key = models.CharField(max_length=128)     # 忘记密码验证码
    
