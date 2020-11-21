# 字符串类型 ""

"""这也是一个乖巧的注释"""

a = "懂王"
b = "睡王"
c = '美国靓丽的风景线'
d = """美国队长4：东西战争"""       # 注释
e = a + b
f = "懂王{}睡王".format("大战")
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
print(f)

# 练习：新建一个字符串，"大吉大利，",分别使用两种方式把"今晚吃鸭"拼在第一个字符串，打印出来。
cj = "大吉大利,今晚吃鸡"
index = cj.find("吃鸭")             # 找到字符串位置
count = cj.count("大")              # 统计字符出现的个数
newcj = cj.replace("鸡", "鸭")      # 替换原有的值为新字符串
lenth = len(cj)                     # 获取字符串长度/字符个数
print(cj)
print(index)
print(count)
print(newcj)
print(lenth)