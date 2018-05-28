# -*- coding: utf-8 -*-
import json

import requests
#固定获取1页10条数据
url="http://comment.ifeng.com/get?job=1&orderby=uptimes&order=DESC&format=json&pagesize=20"

data={
"p":1,
    #这个原连接直接在评论页面的连接中获取
"docurl":"http://news.ifeng.com/a/20180101/54721017_0.shtml"
}

a=requests.post(url,data)
p=json.loads(a.content.decode())
print(type(p))