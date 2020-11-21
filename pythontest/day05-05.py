# 模拟接口登录的完整过程
from dbtools import query

u = input("请输入账号：")
p = input("请输入密码：")

sql = "select * from t_pymysql_account where username = '{}' and password = '{}'".format(u,p)
r = query(sql)         # 调用dbtools里面导入的query方法
print(r)
if len(r) != 0:        # sql查出来的数据不为空，数据表中存在这个账号和密码
    print("登录成功")
else:                  # sql查询的数据为空，数据表中不存在这个账号密码
    print("登录失败")

