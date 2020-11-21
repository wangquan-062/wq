# 首页所有的接口都放到这里
import pytest
import requests
import os, sys
sys.path.append(os.getcwd())

# 方法来表示每个测试用例
def test_01_lbt():
    url = "http://118.24.255.132:2333/get_title_img?num=3"
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200


def test_02_getcoures():
    url = "http://118.24.105.78:2333/getcoures"
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200


def test_03_getquestions():
    url = "http://118.24.105.78:2333/getquestions?num=3"
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200