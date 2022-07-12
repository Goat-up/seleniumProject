import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# wd = webdriver.Chrome()
wd = webdriver.Firefox()
# # 等待元素渲染
wd.implicitly_wait(5)
wd.get('https://dj.gzmky.cn/cmscp/index.do')
try:
    # 登录
    inputBox1 = wd.find_element(By.ID, 'username')
    inputBox2 = wd.find_element(By.ID, 'password')
    button1 = wd.find_element(By.TAG_NAME, 'button')
    inputBox1.send_keys('zonda')
    inputBox2.send_keys('123456')
    button1.click()
    # 获取所有菜单
    aElements = wd.find_elements(By.CSS_SELECTOR, '.sidebar-menu .treeview a')
    # 从上到下依次点击所有功能
    aElements[46].click()
    time.sleep(1)
    aElements[48].click()
    wd.switch_to.frame('centerFrame')

    pswElements = wd.find_elements(By.CSS_SELECTOR, '.row input')
    for pswElement in pswElements:
        pswElement.send_keys("123456")
    wd.back()
except NoSuchElementException:
    pass







        
        







