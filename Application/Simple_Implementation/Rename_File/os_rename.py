# -*- coding: utf-8 -*-
'''修改文件夹下所有文件名称'''
import os
import re

def rename_files():
    file_list = os.listdir(r'C:\Users\linlinle\Downloads\prank')
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r'C:\Users\linlinle\Downloads\prank')
    print(os.getcwd())
    for file_name in file_list:
        os.rename(file_name,re.sub(r'([\d]+)','',file_name))
    os.chdir(saved_path)
    print(os.getcwd())
rename_files()