import requests
u = "http://118.24.105.78:2333/regist"        
h = {"Content-Type":"application/json"} 
d = {"username":"agfhdsgah","password":"a12345678","phone":"18111045678","email":"112a3@qq.com"} 

res = requests.post(url = u , headers = h , json = d )
#print(res.text)
assert res.status_code == 200  
assert res.json()["status"] == 200  
print("成功")