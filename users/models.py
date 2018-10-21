from django.db import models

# from ..strategy.models import *
# from ..travelnote.models import *
from travelnote.models import *
from strategy.models import *

# 登录表
class login(models.Model):
    telephone = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
# 性别表
class sex(models.Model):
    sex = models.CharField(max_length=10)
# 头像表
class icno(models.Model):
    imageurl = models.CharField(max_length=300)
# 用户表
class user(models.Model):
    telephone = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=30)
    state = models.CharField(null=True, max_length=30)
    birthday = models.DateField(null=True,max_length=20)
    mark = models.IntegerField(null=True)
    content = models.TextField(null=True)
    filed1 = models.CharField(null=True, max_length=10)
    filed2 = models.CharField(null=True, max_length=10)
    login = models.ForeignKey(to='login', to_field='telephone', on_delete=models.CASCADE)
    icno = models.ForeignKey(default=1, to='icno', to_field='id', on_delete=models.CASCADE)
    sex = models.ForeignKey(default=1, to='sex', to_field='id', on_delete=models.CASCADE)

# 关注表
class focus(models.Model):
    # 一个人的id
    userid = models.IntegerField()
    uid = models.ForeignKey(to='user', to_field= 'id', on_delete=models.CASCADE)
    # 这个人关注的人的id


# 攻略收藏表
# class collectstrategy(models.Model):
    # userid = models.IntegerField(max_length=15)
    # strategyid = models.IntegerField(max_length=15)
    # scollect = models.ForeignKey(to='strategy', to_field='id', on_delete=True)
    # scollected = models.ForeignKey(to='user', to_field='id', on_delete=True)
# 游记收藏表
# class collecttravelnote(models.Model):
#     userid = models.IntegerField(max_length=15)
#     travelnoteid = models.IntegerField(max_length=15)
#     tcollect = models.ForeignKey(to='travelnote', to_field='id', on_delete=models.CASCADE)
#     tcollected = models.ForeignKey(to='user', to_field='id', on_delete=models.CASCADE)


# 成就表


