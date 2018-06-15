# -*- coding: utf-8 -*-

class CircularQueue:
    '''Queue implementation using circularly linked list for storage.'''
    class _Node:
        __slots__ = '_element','_next'

        def __init__(self,element,next_):
            self._element = element
            self._next = next_

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        oldhead = self._tail._next
        if self._size==1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size +=1

    def rotat(self):
        '''Rotate front element to the back of the queue.'''
        if self._size > 0:
            self._tail = self._tail._next