import time
from selenium import webdriver
from seleniumtools import find_element
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.maximize_window()
driver.get("http://118.24.255.132:9090/shopxo/")

# 手动去登录获得登录之后的cookie
# time.sleep(20)
# print(driver.get_cookie)
# [{'domain': '118.24.255.132', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'e0ar104jvu9rp04hcakjhmuut3'}]

# 使用登录之后的cookie去访问网页，就能绕过登录
driver.delete_all_cookies()
cookie = {'domain': '118.24.255.132', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'e0ar104jvu9rp04hcakjhmuut3'}
driver.add_cookie(cookie)
driver.refresh()