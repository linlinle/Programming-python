# -*- coding: utf-8 -*-
import zipfile, os

#   读取ZIP 文件
os.chdir('C:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist() # ['spam.Txt', 'cats/', 'cats/catnames.Txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.Txt')
print(spamInfo.file_size) # 13908
print(spamInfo.compress_size) # 3828
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))# 'Compressed file is 3.63x smaller!'
exampleZip.close()

#   解压缩
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.extract('spam.Txt') # 'C:\\spam.Txt'
exampleZip.extract('spam.Txt', 'C:\\some\\new\\folders') # 'C:\\some\\new\\folders\\spam.Txt'
exampleZip.close()

#   4.3.3	创建和添加
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.Txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
