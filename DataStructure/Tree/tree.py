# -*- coding: utf-8 -*-
from DataStructure.Queue.linked_queue import LinkedQueue
class Tree:
    '''Abstract base class representing a tree structure.'''
    class Position:

        def element(self):
            raise NotImplementedError(' must be implemented by subclass') #必须由子类实现

        def __eq__(self, other):
            raise NotImplementedError(' must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError(' must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError(' must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError(' must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError(' must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError(' must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1+self.depth(self.parent(p))

    def _height1(self):  # works, but O(n^2) worst-case time
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):  # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p):
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        return self.preorder()
        #return self.postorder()
        #return self.breadthfirst()

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """迭代器"""
        yield p                                         #先对p进行访问
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):  # for each child c
            for other in self._subtree_postorder(c):  # do postorder of c's subtree
                yield other  # yielding each to our caller
        yield p  # visit p after its subtrees

    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)


