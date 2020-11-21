# 模拟登录登录的完整过程
# 两个文件中在同一个模块相互导入
from dbtools import query

u = input("请求输入账号:")
p = input("请求输入密码:")

sql = "select * from t_pymysql_account where username = '{}' and password = '{}'".format(u, p)

res = query(sql)        # 调用dbtools里面导入的query方法
if len(res) != 0:       # 结果长度!=0> sql查出的数据不为空 > 数据表中存在这个账号和密码
    print("登录成功")
else:                   # 结果长度 ==0 > sql查询的数据为空 > 数据表中不存在这个账号和密码
    print("登录失败")