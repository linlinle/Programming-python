
dic = {"apple":10,
       "orange":20,
       "banana":5,
       "rotten tomato":1}
#   x[0]:第一个元素，第二个元素:x[1]
print(sorted(dic.items(), key=lambda x:x[1]))
print(sorted(dic.items(), key=lambda x:x[0]))
print(sorted(dic, key=dic.get))