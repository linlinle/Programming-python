# -*- coding: utf-8 -*-
'''python module queue'''
# import queue
# from collections import deque
class ArrayQueue:
    DEFAULT_CAPACITY = 10                                   #固定大小，循环使用

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY     #是一个具有固定容量的列表实例的引用。
        self._size = 0                                      #表示存储在队列中的元素的当前数量
        self._front = 0                                     #队列第一个元素在数据中的索引

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        '''Return (but do not remove) the element at the front of the queue'''
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        '''Remove and return the first element of the queue'''
        if self.is_empty():
            raise IndexError('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front +1)%len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size)%len(self._data)      #在_data范围内循环使用
        self._data[avail] = e
        self._size += 1

    def _resize(self,cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0

