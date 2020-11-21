import time
from selenium import webdriver
from seleniumtools import find_element
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.maximize_window()
driver.get("http://ctw.testgoup.com/html/login.html")



