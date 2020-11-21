# dict字典 键值对 key-value

# a = {"xm":"张三","xb":"男","nl":"24"}
# #c = {1:"2"}

# b = len(a)
# print(b)
# #print(c["1"])

# #取值
# print(a["xm"])
# print(a.get("xm"))

# #增加
# a["xb"] = "女"
# a["爱好"] = "看书"

# #修改
# a.update({"nl":"27"})

# # 删除
# del a["爱好"]    

# #删除所有
# a.clear()           
# print(a)


# cc = {"mz":"黄忠","hpy":["鲁班","后羿","虞姬"]}
# aa = cc["hpy"]
# print(aa)

dd = {
  "data": {
    "status": True, 
    "token": "f22502461d64704bee62be710nauqgnawb11b4aabcd4569ae0", 
    "userinfo": {
      "headpic": "headimg.jpg", 
      "nickname": "用户7200930", 
      "uid": 1333881176
    }
  }, 
  "msg": "登录成功！", 
  "status": 200
}

print(dd["data"])
print(dd["data"]["token"])
print(dd["data"]["userinfo"])
print(dd["data"]["userinfo"]["uid"])
