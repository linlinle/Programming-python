# -*- coding: utf-8 -*-
"""
小明同学学习了不同的进制之后，拿起了一些数字做起了游戏。小明同学知道，在日常生活中我们最常用的是十进制数，而在计算机中，二进制数也很常用。
现在对于一个数字x，小明同学定义出了两个函数f(x)和g(x)。 f(x)表示把x这个数用十进制写出后各个数位上的数字之和。如f(123)=1+2+3=6。
g(x)表示把x这个数用二进制写出后各个数位上的数字之和。如123的二进制表示为1111011，那么，g(123)=1+1+1+1+0+1+1=6。
小明同学发现对于一些正整数x满足f(x)=g(x)，他把这种数称为幸运数，现在他想知道，大于0且小于等于n的幸运数有多少个？"""

import unittest

def f_or_g(value, system):
    sum = 0
    while value:
        sum += value % system
        value//=system
    return sum

def lucky_number_fg(interval_maximum):
    lucky_number = 0
    for i in range(1, interval_maximum):
        if f_or_g(i, 2) == f_or_g(i, 10):
            lucky_number += 1
        else:
            continue
    return lucky_number

def luckyNumber_map(interval_maximum):
    lucky_number = 0
    for i in range(1,interval_maximum):
        binval = sum(map(int, list(bin(i).replace("0b", ""))))
        decimalval = sum(map(int, list(str(i))))
        if decimalval == binval:
            lucky_number += 1
    return lucky_number

class luckyNumberTestCase(unittest.TestCase):

    def setUp(self):
        self.interval_maximum = 100

    def test_luckyNumber_fg(self):
        self.assertEqual(lucky_number_fg(self.interval_maximum), 3)

    def test_luckyNumber_map(self):
        self.assertEqual(luckyNumber_map(self.interval_maximum),3)

unittest.main()
