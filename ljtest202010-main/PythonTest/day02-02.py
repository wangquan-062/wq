# list 数组/列表:长度和内容可变

# a = [1,2,3]
# # 数组的元素内容：任意数据类型
# # 二维数组 [[1,2,3], ['2','22']]
# a = [1,"12", True, (22,22), ["哒哒哒", "哒哒哒"]]  # a[-1] =  ["哒哒哒", "哒哒哒"]

# # 取值
# print(a)
# # print(a[0])
# # print(a[-1])
# # print(len(a))

# # 添加元素
# a.append(100)
# a.append("123")
# print(a)

# # 修改
# a[0] = 100
# print(a)

# # 删除
# # del a[0]
# a.remove(100)
# print(a)

# print(a.count(True))

# 排序 a = [11,22,23,..]
a = [55,22,33,11,66,77,88,23]
a.sort()                # 从小到大
a.sort(reverse=True)    # 从大到小
print(a)