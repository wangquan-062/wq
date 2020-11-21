import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://www.bilibili.com/")

# step1:获取cookie
# time.sleep(30)
# print(driver.get_cookies())


cookies = [{'domain': '.bilibili.com',  'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': '0145414506af5315ae420e3d7ede2e58'}, 
        {'domain': '.bilibili.com',  'httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': 'a7bbe703%2C1621431875%2Cc99b0*b1'}, 
        {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '376067334'},
        {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': 'ac5qqoj4'},
        {'domain': 'www.bilibili.com', 'httpOnly': False, 'name': 'finger', 'path': '/', 'secure': False, 'value': '158939783'},
        {'domain': '.bilibili.com','httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure': False, 'value': 'AA0A4044-718E-4643-81AC-2E023D2C2471143091infoc'}, 
        {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '35ef735f45ccb7cc'}, 
        {'domain': '.bilibili.com', 'httpOnly': False, 'name': '_uuid', 'path': '/', 'secure': False, 'value': '2924A10F-5E82-DBE6-C5B2-B8F29D0C608553371infoc'}]
driver.delete_all_cookies()
for c in cookies:
    driver.add_cookie(c)

driver.refresh()