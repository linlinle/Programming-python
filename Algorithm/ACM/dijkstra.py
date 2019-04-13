# -*- coding: utf-8 -*-
"""需要三个散列表，Graph、costs、parents"""

import unittest


def find_lowest_cost_node(processed,costs):
    """将节点的所有邻居都存储在散列表"""
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

class DijkstraTestCase(unittest.TestCase):
    def setUp(self):
        self.graph = {}
        self.graph['start'] = {}
        self.graph['start']['a'] = 6
        self.graph['start']['b'] = 2
        self.graph['a'] = {}
        self.graph['a']['end'] = 1
        self.graph['b'] = {}
        self.graph['b']['a'] = 3
        self.graph['b']['end'] = 5
        self.graph['end'] = {}

        self.infinity = float('inf')        # 存储每个节点的开销
        self.costs = {}
        self.costs['a'] = 6
        self.costs['b'] = 2
        self.costs['end'] = self.infinity

        self.parents = {}                   # 存储父节点的散列表
        self.parents['a'] = "start"
        self.parents['b'] = "start"
        self.parents['end'] = None

        self.processed = []                 # 记录处理过的节点

    def test_find_lowest_cost_node(self):
        self.node = find_lowest_cost_node(self.processed,self.costs)  # 在未处理的节点中找出开销最小的节点
        self.assertEqual(self.node,'b')
        while self.node is not None:                                  # 这个 while 循环在所有节点都被处理过后结束
            cost = self.costs[self.node]
            self.neighbors = self.graph[self.node]
            for n in self.neighbors.keys():
                new_cost = cost + self.neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = self.node
            self.processed.append(self.node)
            self.node = find_lowest_cost_node(self.processed,self.costs)

        self.assertEqual(self.costs['end'],6)
unittest.main()



