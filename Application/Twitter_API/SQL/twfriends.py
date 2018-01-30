'''
1.创建带有主键与约束的表。
2.当一个用户（即账号名称）拥有一个逻辑键，我们需要用户的id值。根据People表中是否有该用户，（1）查找People表中的用户，获取该用户的id值，或（2）向People表添加用户，为新增行添加id值。
3.插入一行，表示“粉丝”关系。

'''

import json
import sqlite3
import ssl
import urllib.error

from Application.Twitter_API.OAuth import twurl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()
# 设计表结构时，我们告诉数据库系统强制执行一些规则。这些规则帮助我们避免出错，不要把错误的数据写入表中
#   People表中的name列必须是唯一的（UNIQUE）
cur.execute('''CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
#   Follows表每一行两个数字的组合必须唯一.这些约束避免了多次添加同一个关系
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
            (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #   当提示用户输入一个Twitter账号，如果账号已存在，我们必须找到它的id值。如果People表中还没有该账号，我们必须插入一条记录，并得到该插入行的id值。
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1')
        try:
            (id, acct) = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (acct, )) # 找到它的id值
        try:
            id = cur.fetchone()[0]
        except:
            #   OR IGNORE子句: 表示如果有一个INSERT违反了“name必须唯一”的规则，那么数据库将忽略这个INSERT
            cur.execute('''INSERT OR IGNORE INTO People
                        (name, retrieved) VALUES (?, 0)''', (acct, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('Retrieving account', acct)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed to Retrieve', err)
        break

    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break

    # Debugging
    # print(json.dumps(js, indent=4))

    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        #   使用SELECT语句，检查People表中该账号是或否存在。
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            #   使用fetchone()获取该记录，然后检索返回的元组的第一个（也是唯一）元素，将其存储为friend_id
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except: #   以except代码结束，这意味着，没有发现记录，必须插入新行
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
                        VALUES (?, 0)''', (friend, ))
            conn.commit()
            if cur.rowcount != 1:#  通过cur.rowcount检查有多少行受到影响。由于我们尝试插入一个单行，如果受影响行的数字不是1，那么将导致错误
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid # 如果INSERT执行成功，我们通过cur.lastrowid找出数据库为新建行赋予的id列值
            countnew = countnew + 1
        #   确保不会重复添加同一个Follows关系
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
                    VALUES (?, ?)''', (id, friend_id))
    print('New accounts=', countnew, ' revisited=', countold)
    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()
