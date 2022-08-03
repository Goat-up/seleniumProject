import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("C:/Users/zzh/PycharmProjects/seleniumProject/index.html")
pass
# selectElement = Select(driver.find_element(By.NAME, "box_select"))
# selectElement.select_by_index(1)
# time.sleep(1)
# selectElement.select_by_value("广州")
# time.sleep(1)
# selectElement.select_by_value("上海")
# time.sleep(1)
# selectElement.select_by_visible_text("广州11")
# selectElements = driver.find_elements(By.TAG_NAME, "option")
# selectElement = driver.find_element(By.CSS_SELECTOR, "option[value='深圳']")
# selectElements[2].click()
# selectElement.click()
inputElement = driver.find_element(By.NAME, "inp_type")
inputElement.send_keys("F:/ChromeCoreDownloads/1mmzgw-V1.0.4-release-20220630110201.apk")
# inputElement.click()
# arr = [1,2,2,3,4]
# print(arr.pop())
current = driver.current_window_handle
print(driver.window_handles)
time.sleep(1)
driver.find_element(By.ID, "goto").click()
time.sleep(1)
print(driver.window_handles)
time.sleep(1)
driver.back()


# arr.append(5)
# print(arr)
