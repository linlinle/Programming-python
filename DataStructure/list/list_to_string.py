# -*- coding: utf-8 -*-

# 列表所有元素组合成字符串
def list_print(orin_list):
    stringlist = orin_list[:]
    replace_word = 'and '+stringlist[-1]
    stringlist[-1] = replace_word
    words = ', '.join(stringlist)
    return words
messages = ['apples', 'bananas', 'tofu', 'cats']
print(list_print(messages))


number = [2,"hello",4,5]
print(",".join(map(str,number)))
