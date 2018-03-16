# -*- coding: utf-8 -*-
import shutil, os

#   复制文件和文件夹
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious') # 'C:\\delicious\\spam.txt'
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt') # 'C:\\delicious\\eggs2.txt'
shutil.copytree('C:\\bacon', 'C:\\bacon_backup') # 'C:\\bacon_backup'

#    移动与改名
shutil.move('C:\\bacon.txt', 'C:\\eggs') # 'C:\\eggs\\bacon.txt'
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt') # 'C:\\eggs\\new_bacon.txt

#   永久删除
for filename in os.listdir('.'):
    if filename.endswith('.rxt'):
        os.unlink(filename)
        shutil.rmtree(filename)
