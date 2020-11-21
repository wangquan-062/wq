# 导入webdriver
from selenium import webdriver

# 1.打开浏览器：实例化浏览器句柄（把柄）
# Chrome：大写C
# driver：浏览器操作对象
# executable_path：浏览器驱动文件路径
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.maximize_window()


# 2.访问网址
driver.get("https://www.baidu.com")

# 3.模拟执行测试用例过程
# 3.1输入文字
# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# id定位
driver.find_element_by_id('kw').send_keys("web自动化测试")
# xpath定位
# driver.find_element_by_xpath('//*[@id="su"]').send_keys("web自动化测试")
# name定位
# driver.find_element_by_name('wd').send_keys("web自动化测试")
# classname定位
# driver.find_element_by_class_name('s_ipt').send_keys("web自动化测试")
# css selector定位
# driver.find_element_by_css_selector('#kw').send_keys("web自动化测试")

# 3.2点击搜索按钮
# <input type="submit" id="su" value="百度一下" class="bg s_btn">
driver.find_element_by_id('su').click()

# 超链接
# <a href="http://map.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">地图</a>
# driver.find_element_by_link_text('地图').click()
# 一部分文字定位超链接
# driver.find_element_by_partial_link_text('地').click()

#driver.quit()


