# -*- coding: utf-8 -*-
'''需要三个散列表，Graph、costs、parents'''
#将节点的所有邻居都存储在散列表
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b']= {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}
#存储每个节点的开销
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity
#存储父节点的散列表
parents = {}
parents['a'] = "start"
parents['b'] = "start"
parents['end'] = None
#记录处理过的节点
processed = []

node = find_lowest_cost_node(costs) #在未处理的节点中找出开销最小的节点
while node is not None: #这个 while 循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors= graph[node]
    for n in neighbors.keys():
        new_cost = cost+neighbors[n]
        if costs[n]>new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs['end'])


