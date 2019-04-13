# -*- coding: utf-8 -*-
"""基于线性探测器的符号表"""
import random
class LinearProbingHashMap():
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key  # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)  # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

    def __init__(self, cap=11, p=109345121):
        """
        cap :: 散列表的数组大小(默认尺寸 11)
        p   :: 用于MAD的正素数(默认 109345121)
        """
        self._table = cap * [None]
        self._n = 0  # 散列表中item数目
        self._prime = p  # prime for MAD compression
        self._scale = 1 + random.randrange(p - 1)  # scale from 1 to p-1 for MAD
        self._shift = random.randrange(p)  # shift from 0 to p-1 for MAD
    def __len__(self):
        return self._n
    def hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is object()

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.
          Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j  # mark this as first avail
                if self._table[j] is None:
                    return (False, firstAvail)  # search has failed
            elif k == self._table[j]._key:
                return (True, j)  # found a match
            j = (j + 1) % len(self._table)  # keep looking (cyclically)

    def __getitem__(self, k):
        j = self.hash_function(k)
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))  # no match found
        return self._table[s]._value

    def __setitem__(self, k, v):
        j = self.hash_function(k)
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)  # insert new item
            self._n += 1  # size has increased
        else:
            self._table[s]._value = v  # overwrite existing
    def __delitem__(self, k):
        j = self.hash_function(k)
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))  # no match found
        self._table[s] = object()  # mark as vacated
        self._n -= 1


