# -*- coding: utf-8 -*-

def InsertionSort(S):
    for i in range(1 ,len(S)):
        current = S[i]
        while i > 0 and S[i-1] > current:
            S[i], S[i-1] = S[i-1], S[i]
            i -= 1

def InsertionSort1(S):
    for i in range(1 ,len(S)):
        for j in range(i):
            if S[i-1] > S[i]:
                S[i], S[i - 1] = S[i - 1], S[i]

S = [4,3,5,5,6]
InsertionSort(S)
print(S)