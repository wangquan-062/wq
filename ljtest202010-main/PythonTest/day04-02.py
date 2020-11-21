import time
from selenium import webdriver
# while
a = 1
b = 2

# 死循环 While True:
# while a < b:
#     continue
#     print("a<b")
    # a = a + 1   # 自增
    # break


# while模拟红绿灯显示
# 60， 绿灯30S，黄灯5S，红灯25
#  1-30：打印绿灯
#  31-35： 打印黄灯
#  36-60： 打印红灯


while True:     # 死循环：表示红绿灯一直打印
    # 差一个东西来让红绿灯转起来，每次都去增加一个数
    for i in range(1, 61):
    # 判断60S内的状态：
        if i < 31:
            print("绿灯")
        elif i < 36:
            print("黄灯")
        elif i < 60:
            print("红灯")

        time.sleep(1)       # 代码运行到这儿就卡一秒钟

 