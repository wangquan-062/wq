import pytest
import requests
import os, sys
sys.path.append(os.getcwd())

from utils.dbtools import query
from utils.filetools import read_file,save_file
from utils.common import get_url
from utils.exceltools import read_excel

data = read_excel("./data/测谈网接口.xlsx", "问题详情")

def test_01_question():
    """
        查看问题详情
    """
    u = get_url(data[0][2])
    h = eval(data[0][5])
    res = requests.get(url=u, headers=h)
    assert res.status_code == data[0][6] 
    assert res.json()["status"] == data[0][7]
    print(res.text)
    a = str(res.json()["data"][0]["id"])
    print(a)
    # save file(file_path='./conf/question_id.txt', content= str(res.json()["data"][0]["id"]))


def test_02_getuser4status():
    """
        查看收藏点赞状态
    """
    u = get_url(data[1][2])
    h = eval(data[1][5])
    d = eval(data[1][4])
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == data[1][6]        
    assert res.json()["status"] == data[1][7]
    

def test_03_getcomments():
    """
        查看评论列表成功
    """
    u = get_url(data[2][2])
    h = eval(data[2][5])
    d = eval(data[2][4])
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == data[2][6]        
    assert res.json()["status"] == data[2][7]
    save_file(file_path='./conf/comment_id.txt', content=str(res.json()["data"]["contentlist"][0]['id']))



def test_04_userfellgoods():
    """
        点赞/取消点赞成功
    """
    u = get_url(data[3][2])
    h = eval(data[3][5])
    d = eval(data[3][4])
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == data[3][6]        
    assert res.json()["status"] == data[3][7]

def test_05_usercollections():
    """
        收藏/取消收藏成功
    """
    u = get_url(data[4][2])
    h = eval(data[4][5])
    d = eval(data[4][4])
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == data[4][6]        
    assert res.json()["status"] == data[4][7]

def test_06_new_comment():
    """
        添加评论
    """
    u = get_url(data[5][2])
    h = eval(data[5][5])
    d = eval(data[5][4])
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == data[5][6]    
    assert res.json()["status"] == data[5][7]
    print(res.text)
    sql = "select * from t_user_comments where uid = 1333416969 and fid = 13824 ORDER BY createtime desc limit 1;"
    # sql = "select * from t_user_comments where uid = '{}' and fid = '{}'".format(read_file(file_path ='./conf/user_uid.txt'),read_file(file_path ='./conf/question_id.txt')
    my_comment_id = query(sql)[0][0]
    print(my_comment_id)
    assert len(query(sql)) != 0
    save_file(file_path='./conf/my_comment_id.txt', content=str(my_comment_id))




def test_07_update_comment():
    """
        修改评论
    """
    u = get_url(data[6][2])
    h = eval(data[6][5])
    d = eval(data[6][4])
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == data[6][6]        
    assert res.json()["status"] == data[6][7]
    #sql = "select * from t_user_comments where uid = 1333416969 and fid = 13824 and id = my_comment_id"
    #print(query(sql))
    #assert len(query(sql)) != 0



def test_08_delete_comment():
    """
        删除评论
    """
    u = get_url(data[7][2])
    h = eval(data[7][5])
    d = eval(data[7][4])
    res = requests.post(url=u, headers=h, json=d)
    assert res.status_code == data[7][6]        
    assert res.json()["status"] == data[7][7]

