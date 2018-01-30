# -*- coding: utf-8 -*-
'''每相隔一段时间，打开一次浏览器'''
import webbrowser
import time

break_count = 0

print('the programma start on '+time.ctime())
while (break_count <3 ):
    time.sleep(5)
    webbrowser.open('https://www.bilibili.com/')
    break_count=break_count+1