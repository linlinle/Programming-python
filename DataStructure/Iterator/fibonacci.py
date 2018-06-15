# -*- coding: utf-8 -*-
'''利用generator产生iterator，输出Fibonacci'''

def fibonnacci(n):
    a =0
    b = 1
    for _ in range(n):
        yield a
        temp = a+b
        a = b
        b = temp

if __name__ == '__main__':
    for i in fibonnacci(10):
        print(i)