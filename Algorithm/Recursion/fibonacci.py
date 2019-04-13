# -*- coding: utf-8 -*-
'''利用递归实现'''

def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2)+bad_fibonacci(n-1)

def good_fibonacci(n):
    if n <= 1:
        return n,0
    else:
        (a, b)= good_fibonacci(n-1)
        return (a+b, a)

def list_storage(n):
    arr = [0,1,1]
    while n >arr[-1]:
        arr.append(arr[-1] + arr[-2])
    return arr[-1]
def fast_get(n):
    x,y = 0,1
    while 1:
        if y>=n:return y
        x,y = y, x+y

if __name__ == '__main__':
    print(fast_get(5))