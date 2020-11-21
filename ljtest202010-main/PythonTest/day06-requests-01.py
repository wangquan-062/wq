import requests
from dbtools import query

# url = "http://118.24.105.78:2333/get_title_img"
# h = {"Content-Type":"application/json"}     # 请求头：字典
# res = requests.get(url=url, headers=h)                 # 使用requests去请求get类型的接口
# print(res.text)                         # res.text : 获取返回值

# 1.构造请求
u = "http://118.24.105.78:2333/login" # 地址类型字符串
h = {"Content-Type":"application/json"}     # 请求头：字典
d = {"username":"liuyun1","password":"a123456781"}   # json参数：字典
# post请求
res = requests.post(url=u, headers=h, json=d)
# 2.判断结果
# http状态码
# 结果返回值（结果码）
assert res.status_code == 200   # 预判接口是否有问题
assert res.json()["status"] == 200  # 判断结果码

# 3.数据库查询
sql = "select * from t_user where username = '{}'".format(d["username"])
assert len(query(sql)) != 0
print("登录成功的测试用例执行通过！")

# 练习，使用requests去注册一个测谈网账号
# 一定要使用断言判断结果