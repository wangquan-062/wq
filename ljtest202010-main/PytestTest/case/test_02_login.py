# 这个文件是登录模块的case
import os, sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.dbtools import query
from utils.filetools import read_file, save_file

def test_01_login_success():
    u = "http://118.24.105.78:2333/login"
    h = {"Content-Type":"application/json"}
    d = {"username":"liuyun1","password":"a12345678"}
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    
    # 第三步数据查询
    sql = "select * from t_user where username='{}'".format(d["username"])
    assert len(query(sql)) != 0

    # 保存token
    save_file(content=res.json()["data"]["token"])

