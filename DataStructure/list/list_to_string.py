# -*- coding: utf-8 -*-

# 列表所有元素组合成字符串
def Listprint1(orin_list):
    stringlist = orin_list[:]
    replace_word = 'and '+stringlist[-1]
    stringlist[-1] = replace_word
    words = ', '.join(stringlist)
    return words
messages = ['apples', 'bananas', 'tofu', 'cats']
print(Listprint1(messages))


number = [2,"hello",4,5]
print(",".join(map(str,number)))
