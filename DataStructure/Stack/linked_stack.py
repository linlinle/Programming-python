# -*- coding: utf-8 -*-
'''Implementing a Stack with a Singly Linked List'''

class LinkedStack:
    class _Node:
        __slots__ = '_element','_next'      # __slots__变量限制该class能添加的属性

        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None                   # 链表的第一个node
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e,self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

