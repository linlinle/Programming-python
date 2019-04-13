# -*- coding: utf-8 -*-
"""
手机的九宫格输入法中，输入数字的键位是可以和字母键位对应的。如“2”对应“ABC”，“9”对应“WXYZ”，现假设“1”和“0”为空字符，以此规则试设计一个程序，将单词用一串数字来进行表示。
举例：
输入：cat（不区分大小写）
输出：228
"""
from Application.Simple_Implementation.decorator_timer import timer

@timer
def division_three(s):
    for cha in s.lower():
        if cha >= 'a':
            if cha < 's':
                print((ord(cha)-97)//3 +2,end="")
            elif cha > 's':
                print((ord(cha)-97)//11 + 7,end="")
            else:
                print(7,end="")
        else:
            print(1,end="")
    print()
@timer
def dictionary(word):
    dic = {
    'abc':'2',
	'def':'3',
	'ghi':'4',
	'jkl':'5',
	'mno':'6',
	'pqr':'7',
	'stuv':'8',
	'wxyz':'9'}
    for letter in word:
        for key, value in dic.items():
            if letter in key:
                print(value, end="")
    print()
@timer
def list_index(word):
    a = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    for letter in word:
        for i in range(len(a)):
            if letter in a[i]:
                print(i + 2,end="")
    print()

if __name__ == "__main__":
    word = input().lower()
    while(word != ":wq"):
        #division_three(word)
        dictionary(word)
        #list_index(word)
        word = input()




