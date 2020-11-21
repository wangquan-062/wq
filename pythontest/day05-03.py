# 报错：try>except>finally
# 没有报错: try> else > finally

a = [1,200,3]
try:
    print(a[1])
    print("1")
except:
    print("2")
else:
    print("3")
finally:
    print("4")