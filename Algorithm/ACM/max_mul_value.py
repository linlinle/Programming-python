# -*- coding: utf-8 -*-
"""输入一组数，找出三个相乘最大的值"""

import unittest

def find_max_mul(mul_element):
    max1 = 0; max2 = 0; max3 = 0;min1 = 0; min2 = 0
    for i in mul_element:
        if i !=0:
            if i>max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i>max2:
                max3 = max2
                max2 = i
            elif i>max3:
                max3 = i
            elif i<min1:
                min2 = min1
                min1 = i
            elif i<min2:
                min2 = i
        else:continue
    return max((max1*max2*max3),(max1*min1*min2))

class maxMulValueTestCase(unittest.TestCase):

    def setUp(self):
        self.mul_element = [1,2,3,4,5]

    def test_find_Max_Mul(self):
        self.assertEqual(find_max_mul(self.mul_element), 60)

unittest.main()