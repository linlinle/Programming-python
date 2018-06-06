# -*- coding: utf-8 -*-

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) # 修改元组

#   从第一个开始比较，直到不同的元素
print((0,1,2) < (0,3,4))
print((0,1,2000000) < (0,3,4))

#   单词中字母大小排序
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)

#   字典生成元组
d = {'a': 10, 'b': 1, 'c': 22}
t = list(d.items())
print(t)
for key, val in list(d.items()):
    print(val, key)