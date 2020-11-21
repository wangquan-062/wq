# 异常处理

a = [1,2,3]

try:
    print(a[20])
    print("asdfasdf")
    print("asdfasdf")
    print("asdfasdf")
    print("asdfasdf")
except Exception as e:
    print("代码报错了")
    print("没错，确实报错了")
    print(e)

print("123")