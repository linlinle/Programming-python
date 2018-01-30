# -*- coding: utf-8 -*-

user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

print(user_0.get('first','app'))    #输出原本值
print(user_0.get('first1','app'))   #新建赋值


for key, value in user_0.items():   # 遍历字典
    ...
for key in user_0.keys():   # 遍历键
    ...
for key in sorted(user_0.keys()):   # 按顺序遍历键
    ...
for value in user_0.values():   # 遍历值
    ...

#   嵌套
# 列表中字典
aliens = []
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 字典中列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# 字典中字典
users = {'aeinstein': {'first': 'albert',
                       'last': 'einstein',
                       'location': 'princeton'},
         'mcurie': {'first': 'marie',
                    'last': 'curie',
                    'location': 'paris'},
         }

#   计数器
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0)+1
    # if c not in d:
    #     d[c] = 1
    # else:
    #     d[c] = d[c] + 1
print(d)