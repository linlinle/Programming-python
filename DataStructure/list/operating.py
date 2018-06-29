# -*- coding: utf-8 -*-

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

#   range()创建列表
numbers = list(range(1,6))
print(min(numbers),max(numbers),sum(numbers),len(numbers))
two_number = numbers*2  #  repeats a list a given number of times
print(two_number)

#   列表解析
squares = [value**2 for value in range(1,11)]

#   复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
my_foods.extend(magicians)  #   列表合并
friend_foods = my_foods[:]
print(friend_foods)

#   string into words
s = 'pining for the fjords'
print(s.split())
s = 'spam-spam-spam'
print(s.split('-'))

#  words into string
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
print(delimiter.join(t))

#求交集的两种方式
retA = [i for i in t if i in s]
retB = list(set(t).intersection(set(s)))

# 求并集
retC = list(set(t).union(set(s)))

# 求得两个list的差集
retD = list(set(t).difference(set(s)))

