import time
# import unittest


from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
# wd = webdriver.Firefox()
# # 等待元素渲染
wd.implicitly_wait(5)
wd.get('https://dj.gzmky.cn/cmscp/index.do')

time.sleep(1)
wd.maximize_window()
time.sleep(1)
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
    # 点击所有功能
    aElements[46].click()
    time.sleep(1)
    aElements[48].click()
    wd.switch_to.frame('centerFrame')

    pswElements = wd.find_elements(By.CSS_SELECTOR, '.row input')
    for pswElement in pswElements:
        pswElement.send_keys("123456")
    time.sleep(1)
    wd.back()

    aElements[40].click()
    aElements[41].click()
    # 树形组织-测试组
    wd.switch_to.frame("leftFrame")
    wd.find_element(By.ID, "tree_41_switch").click()
    wd.find_element(By.ID, "tree_43_span").click()
    # 组织列表搜索框

    wd.switch_to.default_content()

    wd.switch_to.frame("centerFrame")
    searchBox = wd.find_element(By.CSS_SELECTOR, "body > div.content > div > div > form.form-inline.ls-search > div:nth-child(3) > input")
    searchButton = wd.find_element(By.CSS_SELECTOR, "body > div.content > div > div > form.form-inline.ls-search > button")
    searchBox.send_keys("123")
    time.sleep(1)
    searchButton.click()
    time.sleep(1)
except NoSuchElementException:
    a = "123"
    print("a=%s" % a)






        
        







