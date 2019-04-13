# -*- coding: utf-8 -*-
import unittest
from DataStructure.Queue.heap_priority_queue import HeapPriorityQueue
import heapq

def heapq_sort(S):
    h = []
    for value in S:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

def heap_sort(lst):
    for start in range(len(lst) - 1, -1, -1):
        siftdown(lst, start, len(lst) - 1)
    for end in range(len(lst) - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    return lst

def siftdown(lst, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[child] > lst[root]:
            lst[child], lst[root] = lst[root], lst[child]
            root = child
        else:
            break

def HPQ_sort(S):
    HQ = HeapPriorityQueue(S.copy())
    for i in range(len(S) - 1, -1, -1):
        HQ._upheap(i)
    for end in range(len(S)-1, -1, -1):
        S[len(S)-end-1] = HQ._data[0]
        HQ._swap(0, len(HQ._data) - 1)  # put minimum item at the end
        HQ._data.pop()  # and remove it from the list;
        HQ._downheap(0)  # then fix new root    return S
    return S

class HeapqSortTestCase(unittest.TestCase):
    def setUp(self):
        self.L = [1,3,5,7,9,2,4,6,8,0]
    def test_HeapqSort(self):
        self.assertEqual(heapq_sort(self.L), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_HPQSort(self):
        self.assertEqual(HPQ_sort(self.L), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

unittest.main()
