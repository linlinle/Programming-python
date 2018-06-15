# -*- coding: utf-8 -*-
from DataStructure.LinkedList.DoubleLinkedBase import _DoubleLinkedBase

class PositionalList(_DoubleLinkedBase):
    '''元素的顺序链表容器允许位置访问'''
    class Position:
        '''表示单个元素位置的抽象'''
        def __init__(self,container,node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not(self == other)   # opposite of __eq__

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError(' p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError(' p is no longer valid')
        return p._node

    def _make_position(self, node):
        '''添加position属性'''
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self,e,predecessor,successor):
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header,self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev,self._trailer)

    def add_before(self, p ,e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

def insertion_sort(L):
    '''Sort PositionalList of comparable elements into nondecreasing order.'''
    if len(L) > 1:
        maker = L.first()
        while maker != L.last():
            pivot = L.after(maker)
            value = pivot.element()
            if value > maker.element():
                maker = pivot
            else:
                walk = maker
                while walk != L.last() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

if __name__ == '__main__':
    l = PositionalList()
    l.add_first(8)
    l.add_last(5)
    l.add_first(9)
    l.add_first(3)
    insertion_sort(l)
    print(l)
