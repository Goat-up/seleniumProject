from selenium.webdriver.common.by import By


class TreeChildSelect:

    def __init__(self, driver2):
        print("TreeChildSelect")
        driver2.implicitly_wait(3)
        driver2.get('https://dj.gzmky.cn/cmscp/index.do')

    @staticmethod
    def selectTreeChild(driver1):
        aElements = driver1.find_elements(By.CSS_SELECTOR, '.sidebar-menu .treeview a')
        # 点击功能
        aElements[46].click()

    @staticmethod
    def loginTest(driver3, username, password):
        inputBox1 = driver3.find_element(By.ID, 'username')
        inputBox2 = driver3.find_element(By.ID, 'password')
        button1 = driver3.find_element(By.TAG_NAME, 'button')
        inputBox1.send_keys(username)
        inputBox2.send_keys(password)
        button1.click()



