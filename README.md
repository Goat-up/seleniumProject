## test selenium
### 下拉选择框
#### 1.直接定位
~~~ 
selectElements = driver.find_elements(By.TAG_NAME, "option")
selectElements[2].click()
~~~
2.Select包
from selenium.webdriver.support.select import Select
~~~
selectElement = Select(driver.find_element(By.NAME, "box_select"))
# method 1
selectElement.select_by_index(1)
time.sleep(1)
# method 2
selectElement.select_by_value("广州")
time.sleep(1)
# method 3
selectElement.select_by_visible_text("深圳")
~~~
### 上传文件
~~~
inputElement = driver.find_element(By.NAME, "inp_type")
inputElement.send_keys("文件路径")
