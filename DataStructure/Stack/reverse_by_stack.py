# -*- coding: utf-8 -*-
from DataStructure.Stack.array_stack import ArrayStack
from DataStructure.Stack.linked_stack import LinkedStack

def reverse_file(file_name):
    '''Overwrite given file with its contents line-by-line reversed.'''
    S = LinkedStack()
    original = open(file_name)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(file_name,'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


if __name__ == '__main__':
    reverse_file('tst.txt')