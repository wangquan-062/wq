# pymysql 使用python连接并且操作mysql数据库
# python的navicat
# 怎么用封装的方法就行，不要求掌握具体的实现
# 步骤  1、pip3 install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
#       2、封装对应查询/修改/删除/插入代码


# 导入pymysql
import pymysql

#封装查询方法
def query(sql):
    # 1、连接msql数据库
    mydb = pymysql.connect(host = "127.0.0.1", user = "root", password ="123456", db = "wq")
    # 2、获取对应的查询窗口：游标
    cur = mydb.cursor()
    # 3、执行查询sql语句
    cur.execute(sql)
    # 4、获取所有的结果
    res = cur.fetchall()
    # 5、关闭数据库连接
    mydb.close()
    return res               # 返回值类型为元组

# 初始化
# a = ()
# b = []
# c = {}

# __name__:python的内置变量
# 通常用在脚本调试
if __name__ == "__main__":        # 如果在当前文件运行，条件满足，如果在其他文件导入，条件不满足
    # sql = "select * from student where sname = "李军""   引号冲突
    sql1 = "select * from student where sname = \"李军\""
    sql2 = 'select * from student where sname = "王芳"'
    sql3 = "select * from student where sname = '王'"
    r1 = query(sql1)
    r2 = query(sql2)
    r3 = query(sql3)
    print(r1)
    print(r2)
    print(r3)