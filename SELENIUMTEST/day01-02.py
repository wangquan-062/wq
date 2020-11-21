from selenium import webdriver
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.maximize_window()
driver.get("https://www.baidu.com")


driver.find_element_by_id('kw').send_keys('web自动化测试')
# e = driver.find_element_by_id('kw')
# print(e)






