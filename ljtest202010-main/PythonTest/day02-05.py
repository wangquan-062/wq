a = '(1,2,3)'
b = tuple(a)
print(type(b))

a = '[1,2,3,4]'
b = list(a)
print(type(b))

a = '{"username":"马云","username1":"马化腾"}'
b = eval(a)
print(type(b))
