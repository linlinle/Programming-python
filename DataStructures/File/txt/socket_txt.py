# -*- coding: utf-8 -*-
import socket
import urllib.request

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:  #   网页通过urllib.urlopen打开后，我们就可以把它当成一个文件，使用for循环来读取
    print(line.decode().strip())#   头部信息仍然会发送，但是urllib代码会处理头部，发送给我们的仅是文件内容