# 异常处理
a = [1,2,3]

try:
    print(a[20])
    print
except Exception as e:
    print("代码报错了")
    print(e)

print("123")