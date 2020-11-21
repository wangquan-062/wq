import time
# while
# a = 1 
# b = 2
# #死循环 while True：
# while a < b:
#     continue
#     print("a < b")
#     # a = a + 1    # 自增
#     # break


# while 模拟红绿灯提示
# 60s：绿灯30s 黄灯5s 红灯25s
# 1-30  绿灯
# 31-35 黄灯
# 36-60 红灯

while True:                     # 死循环表示红绿灯一直打印  
    for i in range(1, 61):      #(1,2,3,4...58,59,60)
    #判断60s内的状态
        if i < 31:
            print("绿灯")
        elif i < 36:
            print("黄灯")
        elif i < 60:
            print("红灯")

        time.sleep(1)           # 代码运行到这里卡1秒钟
 

 


