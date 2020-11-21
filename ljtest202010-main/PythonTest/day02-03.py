# 字典 键值对 key-value

a = {"xm":"刘经康","xb":"女","nl":1400}
# c = {1:"12"}
b = len(a)
print(b)
# print(c)

# 取值
# print(a["xm"])
# print(a.get("xm"))

# 增加
a["爱好"] = '男'
print(a)

# 修改
# a["爱好"] = '男'
a.update({"xb":"男"})
print(a)

# 删除
del a["爱好"]
print(a)

# 删除所有
a.clear()
print(a)


cc = {"mz":"黄陶", "hpy":["张三", "盖伦", "厄加特"]}
a = cc["hpy"]
print(a[0])


dd = {
  "data": {
    "status": True, 
    "token": "7f5414079d984db8059ccee3200000tjl5191188a57a7862e4", 
    "userinfo": {
      "headpic": "headimg.jpg", 
      "nickname": "用户2151411", 
      "uid": 1333569827
    }
  }, 
  "msg": "登录成功！", 
  "status": 200
}

print(dd["data"])
# {'status': True, 'token': '7f5414079d984db8059ccee3200000tjl5191188a57a7862e4', 'userinfo': {'headpic': 'headimg.jpg', 'nickname': '用户2151411', 'uid': 1333569827}}
# dd["data"]["token"]



print(dd["data"]["token"])
