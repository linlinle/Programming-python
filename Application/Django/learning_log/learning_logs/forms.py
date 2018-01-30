# -*- coding: utf-8 -*-
'''根据我们models.py模型中的信息自动创建表单。'''
from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    #最简单的 ModelForm 版本只包含一个内嵌的 Meta 类，它告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段。
    class Meta:
        #    创建一个表单
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}