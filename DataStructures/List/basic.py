# -*- coding: utf-8 -*-

#   基本方法
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'   # 修改
motorcycles.append('ducati')    # 添加
motorcycles.insert(1,'ducati1') # 插入
del motorcycles[0]  # 删除
poped_motocycle= motorcycles.pop(0)  # 删除
motorcycles.remove('ducati')    # 删除


#   组织列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()    #   永久性排序
cars.sort(reverse=True)  # 永久性排序
cars.reverse()  # 反转

sorted(cars)    # 临时排序
len(cars)   # 确定长度


