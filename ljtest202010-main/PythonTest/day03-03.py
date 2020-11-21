

a = int(input("请输入一个年龄："))
if a > 18:              # 19
    print("黄花")
elif a > 12:            # 12 < a <= 19
    print("小黄花")
elif a > 0:             # 0 < a <= 12
    print("小可爱")
else:                   # 所有条件不满足
    print("buzhidao")


if a == 18:
    if b == 12:
        print("")