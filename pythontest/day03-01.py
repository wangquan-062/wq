#if/else
#a = 16

# a = input("请输入一个年龄：")
# a = int(a)
# if a > 17:
#     print("成年人")         # 缩进
# else:
#     print("未成年人")       # 缩进




hege = []
buhege = []
grade = {"张三":58,"张四":90,"张五":88,"张六":59}
for i in grade:
    if int(grade[i]) >= 60:
        hege.append(i)       
    else:
        buhege.append(i)           
print(hege)
print(buhege)






