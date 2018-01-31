# -*- coding: utf-8 -*-

alien_0 = {'x_position': 0, 'y_position': 25}
print("Original position: " + str(alien_0['x_position']))   # 访问字典值
alien_0['speed'] = 'medium'     # 添加键值对
alien_0['x_position'] = alien_0['x_position'] + 2   # 修改字典值

del alien_0['x_position']

#	漂亮打印
import pprint
pprint.pprint(count)