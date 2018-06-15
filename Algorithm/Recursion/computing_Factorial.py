# -*- coding: utf-8 -*-
'''计算阶乘函数的值 O(N)
 n! = n*(n-1)!
'''
def factorial(n):
    if  n == 0:
        return 1
    else:
        return n*factorial(n-1)
