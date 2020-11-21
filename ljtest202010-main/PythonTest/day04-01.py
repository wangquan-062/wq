# 循环语句range（）
# range(11) = (0,1,2,3,4,5,6,7,8,9,10)

# 通过下标遍历元素/数组
# b = ["a", "aasdf", "asdfasdf", ""]
# b = ("a", "aasdf", "asdfasdf", "")
# for i in range(len(b)): # 0-9的序列》元组 [0,...9]
#     # print(i)
#     print(b[i])


# b = ["a", "aasdf", "asdfasdf", ""]
# for i in b:
#     if "aasdf" == i:
#         # continue    # 跳过循环
#         break         # 循环循环
#         print("12312312")
#     else:
#         print(i)


for i in range(1, 10): # 1:总共9条数据 (1,2,3,4,5,6,7,8,9)
    for j in range(1, i+1): # (1, 2)  = (1)
        print('{} x {} = {} \t'.format(j, i, i*j), end=" ")
    print("")

# i = 1 
# for j in range(1, 2) > (1)
# j = 1

# i = 2
# for j in range(1,3) > 1, 2
# j in 

# i = 3
# for j in range(1, 4) > (1,2,3) 
# print

# i = 4
# for j in range(1, 5) > (1,2,3,4)
# print()


# i = 9
# for j in range(1, 10):
# print