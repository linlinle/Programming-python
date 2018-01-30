# -*- coding: utf-8 -*-
import urllib.request

#   打开URL，read方法下载整个文档内容，存入一个字符串变量（如img），将变量内容写入本地文件。
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()


#   区块（或缓冲区）检索数据，在检索下一个区块前将当前区块写入磁盘，防止耗尽内存
img2 = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand2 = open('cover31.jpg', 'wb')
size = 0
while True:
    info = img2.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand2.write(info)
print(size, 'characters copied.')
fhand.close()