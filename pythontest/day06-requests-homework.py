#z 作业
# 用户登录-用户新增文章-用户修改这篇文章
# 要求是在必要的时候必须做完整的校验过程，一定要做数据校验
# 文章表：t_article

import requests
from dbtools import query

# 用户登录
u = "http://118.24.105.78:2333/login"       
h = {"Content-Type":"application/json"}     
d = {"username":"liuyun1","password":"a12345678"}      
res = requests.post(url = u , headers = h , json = d )
assert res.status_code == 200        
assert res.json()["status"] == 200    
sql = "select * from t_user where username = '{}'".format(d["username"])
assert len(query(sql)) != 0
token = res.json()["data"]["token"]
print("用户登录成功！")

# 用户新增文章
u = "http://118.24.105.78:2333/article/new"       
h = {"Content-Type":"application/json","token":token}      
d = { "title":"为11学习测试aaaa",   # 文章标题
      "content":"内容",            # 文章内容
      "tags":"测试测试测试",        # 文章分类
      "brief":"介绍",              # 文章的简介 
      "ximg":"测试jpg.jpg"         # 上传的图片
    }   
res = requests.post(url = u , headers = h , json = d )
#print(res.text)
assert res.status_code == 200        
assert res.json()["status"] == 200 
articleid = res.json()["data"]["articleid"]
sql = "select * from t_article where title = '{}'".format(d["title"])
assert len(query(sql)) != 0
print("文章发表成功!")


# 用户修改这篇文章
u = "http://118.24.105.78:2333/article/update"     
h = {"Content-Type":"application/json","token":token}      
d = { "title":"为11学习测试aa1111",   # 文章标题
      "content":"内容11",            # 文章内容
      "tags":"测试11",               # 文章分类
      "brief":"介绍11",              # 文章的简介 
      "ximg":"测试jpg.jpg",          # 上传的图片
      "aid":articleid                # 文章id
    }   
res = requests.post(url = u , headers = h , json = d )
#print(res.text)
assert res.status_code == 200        
assert res.json()["status"] == 200 
sql = "select * from t_article where id = '{}'".format(d["aid"])
#print(sql)
assert len(query(sql)) != 0
print("文章修改成功!")