# 切换作用域
import time
from selenium import webdriver
from seleniumtools import find_element
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.maximize_window()
driver.get("http://118.24.255.132:9090/shopxo/")
#['CDwindow-981660279FA5334EEE6EC020632BB409', 'CDwindow-B562C1449E002099173421C5A8E0D101']

driver.find_element_by_xpath('//*[@id="floor1"]/div[2]/div[2]/div[1]/a/img').click()

print(driver.window_handles)
driver.switch_to_window(driver.window_handles[-1])
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button').click()
