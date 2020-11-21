import os, sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.dbtools import query
from utils.filetools import read_file, save_file


def test_01_new_aritcle():
    """
        新建文章case
    """
    u = "http://118.24.105.78:2333/article/new"
    h = {"Content-Type":"application/json","token":read_file()}
    d = {"title":"为什么要学习测试","content":"内容","tags":"测试123","brief":"介绍","ximg":"dsfsdf.jpg"}
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    print(res.text)
    # 数据库查询
    aid = res.json()["data"]["articleid"]
    sql = "select * from t_article where id = {}".format(aid)
    assert len(query(sql)) != 0