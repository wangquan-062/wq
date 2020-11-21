
# 参数
# def add(a=10, b=10):
#     return a + b


# a = add()
# print(a)

def user_login(username, password):
    if username == "test" and password == "123456":
        print("登录成功")
    else:
        print("登录失败")

u = input("请输入账号:")
p = input("请输入密码:")

user_login(u, p)
