# -*- coding: utf-8 -*-

def BubbleSort(S):
    for i in range(len(S) - 1):
        for j in range(len(S) - i - 1):
            if S[j] > S[j+1]:
                S[j] , S[j+1] = S[j+1], S[j]

    return S

S = [45, 32, 8, 33, 12, 22, 19, 97]
BubbleSort(S)
print(S)

