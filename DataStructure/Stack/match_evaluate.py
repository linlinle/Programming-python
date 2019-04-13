# -*- coding: utf-8 -*-
from DataStructure.Stack.array_stack import ArrayStack
from DataStructure.Stack.linked_stack import LinkedStack


def match_math(expr):
    '''Return True if all delimiters are properly match; False otherwise.'''
    lefty = '({['
    righty = ')}]'
    S = LinkedStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

def Evaluate(expr):
    ops = LinkedStack()
    vals = LinkedStack()
    for i in expr:
        if i == '(':
            pass
        elif i == '+':
            ops.push(i)
        elif i == '-':
            ops.push(i)
        elif i == '*':
            ops.push(i)
        elif i == '/':
            ops.push(i)
        elif i == '//':
            ops.push(i)
        elif i == ')': # 如果字符为）,弹出运算符合操作数，计算结果并压入栈
            op = ops.pop()
            v = vals.pop()
            if op == '+':
                v = vals.pop() + v
            if op == '-':
                v = vals.pop() - v
            if op == '*':
                v = vals.pop() * v
            if op == '/':
                v = vals.pop() / v
            if op == '//':
                v = vals.pop()//v
            vals.push(v)
        else:
            vals.push(int(i))
    return vals.pop()


if __name__ == '__main__':
   print( Evaluate('(1+(2*2))'))