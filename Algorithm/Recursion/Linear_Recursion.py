# -*- coding: utf-8 -*-
'''线性递归:递归调用最多从一个开始'''

def linear_sum(S,n):
    if n==0:
        return 0 # 0+S[0]
    else:
        return linear_sum(S,n-1)+S[n-1]

def reverse(S,start,stop):
    if start < stop - 1:
        S[start],S[stop] = S[stop],S[start]     #同时赋值
        reverse(S,start+1,stop-1)
        # start, stop = start+1,stop-1      非递归版本



def power(x, n):
    '''power(x,n) = x*power(x,n-1)'''
    if n==0:
        return 1
    else:
        return x * power(x,n-1)
