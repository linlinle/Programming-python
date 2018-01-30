# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('music.sqlite')  # 与当前目录中music.sqlite3数据库文件建立“连接”
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')  #   如果Track表已经存在，就移除Tracks表
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')# 创建Tracks表，包括文本型的title列与整数型的plays列

#   INSERT操作，向表中添加一些数据
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',('Thunderstruck', 20))
#   指定值为(?, ?)，这表示实际值通过第二个参数的一个元组(’My Way’, 15)来传递
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',('My Way', 15))
conn.commit()   #提交命令将数据写入数据库文件

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')  # 检索刚插入表中的行
#   为了提高效率，当执行SELECT语句时，游标并不会从数据库中读取所有数据。相反，数据是在for循环时按需读取。
for row in cur:
    print(row)
cur.execute('DELETE FROM Tracks WHERE plays < 100')
#   UPDATE语句对一行或多行的一个列或多列进行更新
cur.execute("UPDATE Tracks SET plays = 16 WHERE title = 'My Way'")

conn.close()