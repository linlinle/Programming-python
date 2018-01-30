# -*- coding: utf-8 -*-
from urllib import request
import re

def read_text():
    with open('movie_quotes.txt','r') as f:
        lines = f.readlines()
    odom = ''
    for line in lines:
        odom += line.rstrip() # 将单个数据分隔开存好
    odom= re.sub(',|\.|\(|\)','',odom)
    odom = re.sub(' ', '%20', odom)
    print(odom)
    check_profanity(odom)

def check_profanity(text_to_check):
    hosts = 'http://www.wdylike.appspot.com/?q='+(text_to_check)
    print(hosts)
    connection = request.urlopen(hosts)
    output = connection.read()
    print(output)
    connection.close()

read_text()