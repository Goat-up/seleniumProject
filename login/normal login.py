import this

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def login(url, username, password):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    wd.get(url)
    try:
        input_box1 = wd.find_element(By.ID, 'username')
        input_box2 = wd.find_element(By.ID, 'password')
        button1 = wd.find_element(By.TAG_NAME, 'button')
        input_box1.send_keys(username)
        input_box2.send_keys(password)
        button1.click()
    except NoSuchElementException:
        pass
    return 0


def fun(url):
    wd = webdriver.Firefox()
    wd.get(url)


print("id name className tagName link partyLink cssSelector xPath")

