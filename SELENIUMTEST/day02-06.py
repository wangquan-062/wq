import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://www.bilibili.com/")


#step1:获取cookie
time.sleep(30)
print(driver.get_cookies())



# cookies = [{'domain': '.bilibili.com', 'expiry': 1700487886, 'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure': False, 'value': '0FBBCCB9-BFB2-471B-A83B-7DF633FE10A4143108infoc'}, 
# {'domain': '.bilibili.com', 'expiry': 1637415886, 'httpOnly': False, 'name': '_uuid', 'path': '/', 'secure': False, 'value': '6F13984B-7FF2-3C41-0F98-280B84F7A78B86598infoc'}, 
# {'domain': 'www.bilibili.com', 'httpOnly': False, 'name': 'finger', 'path': '/', 
# 'secure': False, 'value': '-53268994'}]

# driver.delete_all_cookies()
# for c in cookies:
#     driver.add_cookie(c)

# driver.refresh()


