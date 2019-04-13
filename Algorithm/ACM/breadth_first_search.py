# -*- coding: utf-8 -*-
"""寻找芒果销售商,创建一个朋友名单,依次检查名单中的每个人，看看他是否是芒果销售商"""
import unittest
from collections import deque

def person_is_seller(name):
    return name[-1] =='m'                       #最后一个字母为'm'

def search(graph,name):
    search_queue = deque()
    search_queue += graph[name]                 # 获取所有邻居
    while search_queue:                         #只要队列不为空
        person = search_queue.popleft()         # 就取出其中的第一个人
        if person_is_seller(person):            #检查这个人是否是芒果销售商
            print(person+' is a mango seller!')
            return True
        else:
            search_queue +=graph[person]        #不是芒果销售商。将这个人的朋友都加入搜索队列
    return False

class BreadthSearchTest(unittest.TestCase):
    def setUp(self):
        self.graph = {}
        self.graph["you"] = ["alice", "bob", "claire"]
        self.graph["bob"] = ["anuj", "peggy"]
        self.graph["alice"] = ["peggy"]
        self.graph["claire"] = ["thom", "jonny"]
        self.graph["anuj"] = []
        self.graph["peggy"] = []
        self.graph["thom"] = []
        self.graph["jonny"] = []

    def test_search(self):
        self.assertTrue(search(self.graph,'you'))

unittest.main()

