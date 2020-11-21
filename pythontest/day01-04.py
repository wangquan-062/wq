# 拼接数据
# a = "大吉大利"
# b = "今晚吃鸡"
# c = b + a
# d = "{}大吉大利".format("今晚吃鸡")      # 拼接数据
# print(a)
# print(b)
# print(c)
# print(d)

cj = "今晚吃鸡，大吉大利"
index = cj.find("大利")
count = cj.count("大")
newcj = cj.replace("鸡","鸭")
lenth = len(cj)

print(index)
print(count)
print(newcj)
print(lenth)