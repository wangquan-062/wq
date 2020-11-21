import requests
from dbtools import query

# 登录
u = "http://118.24.105.78:2333/login" # 地址类型字符串
h = {"Content-Type":"application/json"}     # 请求头：字典
d = {"username":"liuyun1","password":"a12345678"}   # json参数：字典
res = requests.post(url=u, headers=h, json=d)
assert res.status_code == 200 
assert res.json()["status"] == 200 
sql = "select * from t_user where username = '{}'".format(d["username"])
assert len(query(sql)) != 0

token = res.json()["data"]["token"]
print("用户登录成功")

# 关联用户退出
u = "http://118.24.105.78:2333/logout"
h = {"Content-Type":"application/json","token":token}
r = requests.get(url=u, headers=h)
assert res.status_code == 200 
assert res.json()["status"] == 200 

print("用户退出成功")


# 作业
# 1.用户登录-用户新增文章-用户修改这篇文章
# 要求是在必要的时候必须做完整的校验过程，一定要做数据验证
# 文章表：t_article
