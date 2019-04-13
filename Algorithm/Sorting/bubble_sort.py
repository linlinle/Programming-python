# -*- coding: utf-8 -*-
import unittest

def bubble_sort(S):
    for i in range(len(S) - 1):
        for j in range(len(S) - i - 1):
            if S[j] > S[j+1]:
                S[j] , S[j+1] = S[j+1], S[j]
    return S

class BubbleSortTestCase(unittest.TestCase):
    def setUp(self):
        self.S = [45, 32, 8, 33, 12, 22, 19, 97]
    def test_BubbleSort(self):
        self.assertEqual(bubble_sort(self.S),[8, 12, 19, 22, 32, 33, 45, 97])

unittest.main()


