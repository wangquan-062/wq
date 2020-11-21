#注册
import requests
from dbtools import query

# 1.构造请求
import requests
u = "http://118.24.105.78:2333/regist"        
h = {"Content-Type":"application/json"} 
d = {"username":"fhdsggah","password":"a12345g678","phone":"18111044678","email":"112a31@qq.com"} 
res = requests.post(url = u , headers = h , json = d )

# 2.判断结果
assert res.status_code == 200  
assert res.json()["status"] == 200  

# 3.数据库查询
sql = "select * from t_user where username = '{}'".format(d["username"])
assert len(query(sql)) != 0
print("登录成功的测试用例执行通过！")