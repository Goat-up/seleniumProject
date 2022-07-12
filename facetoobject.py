import main
from selenium import webdriver

driver = webdriver.Chrome()
a = main.TreeChildSelect(driver)
a.loginTest(driver, "zonda", "123456")
a.selectTreeChild(driver)
driver.quit()
