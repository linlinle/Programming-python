# -*- coding: utf-8 -*-
from collections import MutableMapping

class MapBase(MutableMapping):
  """Our own abstract base class that includes a nonpublic _Item class.
  集合模块提供了两个与当前讨论相关的抽象基类:Mapping和MutableMapping类。Mapping类包含Python的dict类支持的所有非突变方法，而MutableMapping类扩展该方法以包含突变方法。
  """

  #------------------------------- nested _Item class -------------------------------
  class _Item:
    """Lightweight composite to store key-value pairs as map items."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __eq__(self, other):
      return self._key == other._key   # compare items based on their keys

    def __ne__(self, other):
      return not (self == other)       # opposite of __eq__

    def __lt__(self, other):
      return self._key < other._key    # compare items based on their keys
