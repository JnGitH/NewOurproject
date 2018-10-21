from django.db import models

from users.models import *
# 封面
class tcover(models.Model):
    url = models.TextField()

# 帖子状态
class condition(models.Model):
    condition = models.CharField(max_length=20)

# 游记
class travelnote(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(max_length=20)
    good = models.IntegerField()
    view = models.IntegerField()
    state = models.CharField(max_length=200)
    file1 = models.CharField(max_length=200, null=True)
    file2 = models.CharField(max_length=200, null=True)
    userid = models.ForeignKey(to="users.user",to_field="id",on_delete= models.CASCADE)

    condition = models.ForeignKey(to='condition',to_field='id', on_delete=models.CASCADE)
    cover = models.ForeignKey(to='tcover',to_field='id',on_delete=models.CASCADE)
# 图片
class timages(models.Model):
    url = models.TextField()
    timages = models.ForeignKey(to='travelnote', to_field='id',on_delete=models.CASCADE)


# 内容
class tcontent(models.Model):
    contentt = models.TextField(default='not have message')
    tid = models.ForeignKey(to='travelnote', to_field='id', on_delete=models.CASCADE)

# 游记收藏
class tcollection(models.Model):
    userid = models.ForeignKey(to='users.user',to_field='id',on_delete=models.CASCADE)
    tid = models.ForeignKey(to='travelnote', to_field='id', on_delete=models.CASCADE)

