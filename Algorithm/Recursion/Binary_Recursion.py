# -*- coding: utf-8 -*-
'''二分递归：递归调用启动了另外两个调用'''

def binary_sum(S,start,stop):
    '''Return the sum of the numbers in implicit slice S[start:stop].'''
    if start >= stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start + stop)//2
        return binary_sum(S,start,mid) + binary_sum(S,mid,stop)