# if/else

# a = 16
# if a > 17:  # 条件语句
#     print("成年人")
# else:
#     print("未成年人")

# a = int(input("请输入一个年龄:"))
# a>=18 > a == 18; a>18
# a<=18 > a == 18 or a< 18
# if a < 17:
#     print("再见！")
# else:
#     print("花姑娘，哟西")
    

# name = input("请输入一个名字：")
# age = int(input("请输入ta的年龄:"))
# if name == "刘经康" and age != 35:
#     print("刘7K日元")
# else:
#     print("100E津巴布韦币")

# 小练习：有一个字典，比较成绩
user = {'刘经康':80, '郭红艳':90}
u1 = user["刘经康"]
u2 = user['郭红艳']
if u1 > u2:
    print('刘经康成绩更高')
else:
    print('郭红艳更厉害')


# 练习：请输入两个人的姓名和成绩，{'刘经康':80, '郭红艳':90}
# 然后输出成绩更好的名字

u1 = input("请输入名字1：")
y1 = int(input("请输入名字1的年龄："))
u2 = input("请输入名字2：")
y2 = int(input("请输入名字2的年龄："))

account = {}
account[u1] = y1
account[u2] = y2
if account[u1] > account[u2]:
    print("这个兄弟更厉害, {}".format(u1))
else:
    print("这个兄弟更厉害, {}".format(u2))
