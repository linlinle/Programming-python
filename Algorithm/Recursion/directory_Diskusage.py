# -*- coding: utf-8 -*-
'''计算目录下的磁盘使用大小'''
import os
def disk_usage(path):
    total = os.path.getsize(path) # 返回 path 参数中文件的字节数,不包括文件夹
    if os.path.isdir(path):       #确定是文件夹
        for filename in os.listdir(path):   #遍历目录
            child_path = os.path.join(path,filename)
            total += disk_usage(child_path)

    print('{0:7}'.format(total),path) #每次回调时打印
    return total

if __name__ == '__main__':
    disk_usage('./')
