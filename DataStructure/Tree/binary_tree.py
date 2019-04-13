# -*- coding: utf-8 -*-
from DataStructure.Tree.tree import Tree
class BinaryTree(Tree):
    '''Abstract base class representing a binary tree structure.'''
    def left(self, p):
        raise NotImplementedError(' must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError(' must be implemented by subclass')

    def sibling(self, p):
        '''返回兄弟结点位置'''
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield  self.right(p)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        return self.inorder()