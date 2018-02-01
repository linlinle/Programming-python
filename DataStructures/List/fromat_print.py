# -*- coding: utf-8 -*-
def printTable(origin_list):
    max_size = len(max(max(origin_list, key=len), key=len)) #   查找最长的字符串
    for (i,j,k) in zip(*origin_list):
        print(i.rjust(max_size),j.ljust(max_size),k.ljust(max_size))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
