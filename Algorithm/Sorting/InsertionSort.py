# -*- coding: utf-8 -*-

def InsertionSort(S):
    for i in range(1 ,len(S)):
        current = S[i]
        while i > 0 and S[i-1] > current:
            S[i], S[i-1] = S[i-1], S[i]
            i -= 1

S = [4,3,5,56]
InsertionSort(S)
print(S)