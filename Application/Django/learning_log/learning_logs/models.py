from django.db import models
from django.contrib.auth.models import User
# Create your module here.

class Topic(models.Model):
    '''用户学习的主题'''
    # CharField：存储少量文本
    # max_length：告诉Django该在数据库中预留多少空间
    text = models.CharField(max_length=200)
    # DateTimeField：记录日期和时间的数据
    # auto_now_add：每当用户创建新主题，这都让Django将这个属性自动设置成当前日期和时间
    date_added = models.DateTimeField(auto_now_add=True)
    #   建立到模型 User 的外键关系
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    # 显示模型的简单表示
    def __str__(self):
        '''返回模型字符串表示'''
        return self.text

class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # 存储用于管理模型的额外信息
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50]+'...'