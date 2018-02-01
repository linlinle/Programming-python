# -*- coding: utf-8 -*-
def Listprint(orin_list):
    stringlist = orin_list[:]
    words = ''
    stringlist.insert(-1,'and')
    for word in stringlist[:-2]:
        words += (word+', ')
    words = words + stringlist[-2] + ' ' + stringlist[-1]
    return words

# 另一个方法join
def Listprint1(orin_list):
    stringlist = orin_list[:]
    replace_word = 'and '+stringlist[-1]
    stringlist[-1] = replace_word
    words1 = ', '.join(stringlist)
    return words1

messages = ['apples', 'bananas', 'tofu', 'cats']

print(Listprint(messages))
print(Listprint1(messages))
