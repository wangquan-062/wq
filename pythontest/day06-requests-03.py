import requests
from dbtools import query

# 登录
u = "http://118.24.105.78:2333/login"        # 地址类型是字符串
h = {"Content-Type":"application/json"}       # 请求头：字典
d = {"username":"liuyun1","password":"a12345678"}         # json参数：字典
res = requests.post(url = u , headers = h , json = d )

assert res.status_code == 200          # 预判接口是否有问题
assert res.json()["status"] == 200     # 判断结果码

sql = "select * from t_user where username = '{}'".format(d["username"])
assert len(query(sql)) != 0

token = res.json()["data"]["token"]
print("用户登录成功！")

# 关联用户退出
u = "http://118.24.105.78:2333/logout"
h = {"Content-Type":"application/json","token":token}  
requests.get(url = u,headers =h)

assert res.status_code == 200       
assert res.json()["status"] == 200  
print("用户退出成功！")





