from django.db import models


class Area(models.Model):
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.area


class Post(models.Model):
    # 名字
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # 电话
    tel = models.IntegerField(null=True, default=0)
    # 时间
    time = models.DateField(auto_now=True)
    # 地区
    area = models.ForeignKey(Area)
    # 评分
    score = models.IntegerField(default=5)
    # 人均
    average = models.IntegerField(default=10)
