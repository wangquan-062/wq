# 方法：模板/工具，直接调用就可以实现复用

def add(a, b):
    sum = a + b
    return sum

def jianfa(a, b):
    return a - b

def chengfa(a, b):
    print("这是个乖巧的乘法")
    print("这是个乖巧的乘法")
    print("这是个乖巧的乘法")
    print("这是个乖巧的乘法")

# 命名规则
def admin_login(username, password):
    pass    # 占位

chengfa(1, 10)
# a = 1 + 1
# b = 2 + 2

a = add(1, 1)
b = add(2, 2)

print(a, b)

c = jianfa(2, 1)
print(c)
