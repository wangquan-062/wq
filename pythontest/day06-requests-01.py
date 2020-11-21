import requests
from dbtools import query

# url = "http://118.24.105.78:2333/get_title_img"
# res = requests.get(url)                    # 表示使用requests去请求get类型的接口
# print(res.text)                            # res.text：获取返回值


# 1.构造请求
# 登录举例
u = "http://118.24.105.78:2333/login"        # 地址类型是字符串
h = {"Content-Type":"application/json"}       # 请求头：字典
d = {"username":"liuyun1","password":"a12345678"}                                             # json参数：字典
# post请求
res = requests.post(url = u , headers = h , json = d )
# print(res.text)

# 2.判断结果
# http状态码
# 结果返回值(结果码)
# if res.status_code == 200:
#     print("状态码正常，接口正常")
# else:
#     print("接口异常")
# 自动化测试一般不使用if else语句，使用断言判断

assert res.status_code == 200          # 预判接口是否有问题
assert res.json()["status"] == 200     # 判断结果码
print("成功")


# 3.数据库查询
sql = "select * from t_user where username = '{}'".format(d["username"])
# print(sql)
assert len(query(sql)) != 0
print("登录成功的测试用例执行通过！")



