# -*- coding: utf-8 -*-

def BubbleSort(S):
    for i in range(len(S) - 1):
        for j in range(len(S) - i - 1):
            if S[j] > S[j+1]:
                S[j] , S[j+1] = S[j+1], S[j]

