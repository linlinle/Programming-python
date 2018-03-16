# -*- coding: utf-8 -*-
import os
count = 0
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.txt') :
           # Windows上使用反斜杠（\）来构造文件路径，Linux和Mac上使用正斜杠（/）来构造文件路径。os.path.join知道如何处理这一差异，
           # 能够识别当前运行的操作系统，据此选择适合的连接。
           thefile = os.path.join(dirname, filename)    # 目录中的文件名与目录名连接在一起
           print(os.path.getsize(thefile), thefile)
           count = count + 1
           fhand = open(thefile, 'r')
           lines = list()
           for line in fhand:
               lines.append(line)
           if len(lines) == 3 and lines[2].startswith('Sent from my iPhone'):   #第三行以Sent开头。
               os.remove(thefile)
               continue

print('Files:', count)