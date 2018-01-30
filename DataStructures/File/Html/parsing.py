# -*- coding: utf-8 -*-
import  urllib.request
import re
from bs4 import BeautifulSoup
import ssl


url ='http://www.py4e.com/book.htm'
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
req = urllib.request.Request(url=url, headers=headers)
html = urllib.request.urlopen(req).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(req, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')    # 先匹配 '<a'
for tag in tags:
    print(tag.get('href', None))    #   再匹配 'href='