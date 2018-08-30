"""
    查找列表中频率最高的值
"""

a = [1,2,3,1,2,3,2,2,4,5,1]
print(max(set(a),key=a.count))

"""using Counter from collections """
from collections import Counter
#   返回字典的形式
cnt = Counter(a)
# 直接返回字典形式
dictory = dict(Counter(a))
print(cnt.most_common(1))

"""检查两个字符串是不是由相同字母不同顺序组成"""
print(Counter("abc") == Counter("aac"))