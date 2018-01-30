# -*- coding: utf-8 -*-
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

with open(filename) as file_object:
    # strs = file_object.read()
    # line = file_object.readline()
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string = line.rstrip()   # 删除字符串末尾空白
    if line.startswith('I also'):   #   匹配开头的一行
        continue
    print(pi_string)



