'''如果在没有重新爬取网页的情况下再次计算网页排名，你可以用sprest.py程序重置，然后重启sprank.py'''
import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''UPDATE Pages SET new_rank=1.0, old_rank=0.0''')
conn.commit()

cur.close()

print("All pages set to a rank of 1.0")
