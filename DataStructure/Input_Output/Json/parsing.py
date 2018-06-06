# -*- coding: utf-8 -*-
import json

data = '''
[
    { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    } ,
    { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''
info = json.loads(data)     # 得到一个Python列表
print('User count:', len(info))
for item in info:           # 列表的每个数据项是一个Python字典
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
