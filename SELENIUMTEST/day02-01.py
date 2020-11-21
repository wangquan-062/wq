import time
from selenium import webdriver
from seleniumtools import find_element
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.maximize_window()
driver.get("http://118.24.255.132:9090/shopxo/")

searchid = ('id','search-input')
topsearchid = ('id','ai-topsearch')
a = ('xpath','/html/body/div[4]/div/ul/li/div/a/p')

find_element(driver,searchid).send_keys('包包')
find_element(driver,topsearchid).click

e = find_element(driver,a)
assert e.text == '纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条'
print("没问题")
