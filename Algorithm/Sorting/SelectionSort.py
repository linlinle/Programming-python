# -*- coding: utf-8 -*-
from DataStructure.Queue.PriorityQueue import SortedPriorityQueue,UnsortedPriorityQueue
def SelectionSort(S):
    for i in range(len(S) - 1):
        min = i
        for j in range(i+1, len(S)):
            if S[min] > S[j]:
                min = j
        S[i], S[min] = S[min], S[i]


def SelectionSortPriorityQueue(S):
    PQ = SortedPriorityQueue()
    for i in S:
        PQ.add(i,i)
    for i in range(len(S)):
        S[i] = PQ.remove_min()



S = [1,32,4,5]
SelectionSortPriorityQueue(S)
print(S)