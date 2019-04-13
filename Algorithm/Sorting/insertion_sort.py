# -*- coding: utf-8 -*-
import unittest

def insertion_sort(S):
    for i in range(1 ,len(S)):
        current = S[i]
        while i > 0 and S[i-1] > current:
            S[i], S[i-1] = S[i-1], S[i]
            i -= 1
    return S

class InsertionSortTestCase(unittest.TestCase):
    def setUp(self):
        self.S = [4,3,5,5,6]
    def test_InsertionSort(self):
        self.assertEqual(insertion_sort(self.S), [3, 4, 5, 5, 6])

unittest.main()