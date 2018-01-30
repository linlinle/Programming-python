# -*- coding: utf-8 -*-
import os

print(os.getcwd())  # 当前工作目录
print(os.path.abspath('memo.txt'))  #文件的绝对路径
print(os.path.join(os.getcwd(),'memo.txt')) # 路径添加
print(os.path.exists('memo.txt'))   # 检查文件或目录是否存在
print(os.path.isdir('music'))
print(os.path.isfile('pi_digits.txt'))
print(os.listdir(os.getcwd()))