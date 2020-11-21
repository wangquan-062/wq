import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.maximize_window()
driver.get("http://118.24.255.132:9090/shopxo/")

# 输入文字
# <input id="search-input" name="wd" type="text" placeholder="其实搜索很简单^_^ !" value="" autocomplete="off">
# id定位
driver.find_element_by_id('search-input').send_keys('包包')
# xpath定位：//*[@id="search-input"]
#driver.find_element_by_xpath('//*[@id="search-input"]').send_keys('包包')

# 点击搜索
# <input id="ai-topsearch" class="submit am-btn" index="1" type="submit" value="搜索">
driver.find_element_by_id('ai-topsearch').click()
# time.sleep(5)                # 固定等待
# driver.implicitly_wait(5)    # 隐式等待，智能的判断网页是否加载完
# 显式等待


# 断言结果
res = driver.find_element_by_xpath('/html/body/div[4]/div/ul/li/div/a/p')
assert res.text == '纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条'
# e = driver.find_elements_by_id('search-input')
# print(e)
# assert len(e) != 0
print("没问题")


