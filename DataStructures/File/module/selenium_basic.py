# -*- coding: utf-8 -*-

#   启动 selenium 控制的浏览器
from selenium import webdriver
browser = webdriver.Firefox()
print(type(browser)) #  <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('http://inventwithpython.com')

#   在页面中寻找元素
#find_element_*方法返回页面中匹配查询的第一个元素。find_elements_*页面中所有匹配的元素。
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.') # Found <img> element with that class name!

#   点击页面
linkElem = browser.find_element_by_link_text('Read It Online')
print(type(linkElem)) # <class 'selenium.webdriver.remote.webelement.WebElement'>
print(linkElem.click()) # follows the "Read It Online" link

#   填写并提交表单
browser = webdriver.Firefox()
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('not_my_real_email@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

#   发送特殊键
# 如果光标当前不在文本字段中，按下 home 和 end 键，将使浏览器滚动到页面的顶部或底部。
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scrolls to bottom
htmlElem.send_keys(Keys.HOME) # scrolls to top


#   模拟点击各种浏览器按钮
browser.back() #    点击“返回”按钮
browser.forward() # 点击“前进”按钮。
browser.refresh() # 点击“刷新”按钮。
browser.quit() # 点击“关闭窗口”按钮。
