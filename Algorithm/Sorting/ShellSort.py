# -*- coding: utf-8 -*-

def ShellSort(S):
    L = len(S)
    h = 1
    while h <= L/3:
        h = h*3 + 1
    while h >= 1:
        for i in range(h, L):
            current = S[i]
            while i >= h and S[i - h] > current:
                S[i], S[i - h] = S[i - h], S[i]
                i -= h
        
        h = int(h/3)
S = [4,3,5,5,6,1,1,3,46256,5,66,562,6,46,2]
ShellSort(S)
print(S)