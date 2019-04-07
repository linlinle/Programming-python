# -*- coding: utf-8 -*-
"""基于拉链法的散列函数"""
import random

class SeparateChainingHashMap():

    def __init__(self, cap=11, p=109345121):
        """
        cap :: 散列表的数组大小(默认尺寸 11)
        p   :: 用于MAD的正素数(默认 109345121)
        """
        self._table = cap * [None]
        self._n = 0                                    # 散列表中item数目
        self._prime = p                                # prime for MAD compression
        self._scale = 1 + random.randrange(p - 1)      # scale from 1 to p-1 for MAD
        self._shift = random.randrange(p)              # shift from 0 to p-1 for MAD

    def __len__(self):
        return self._n
    def hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __getitem__(self, k):
        j = self.hash_function(k)
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))  # no match found
        return bucket[k]

    def __setitem__(self, k, v):
        j = self.hash_function(k)
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  # UnsortedTableMap类依赖于在Python列表中以任意顺序存储键-值对
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def __delitem__(self, k):
        j = self.hash_function(k)
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]
        self._n -= 1
