# -*- coding: utf-8 -*-
import re
# def fibo(num):
#     numList = [0,1]
#     for i in range(num - 2):
#         numList.append(numList[-2] + numList[-1])
#     return numList
# a=fibo(4)
# print a


#第n天 有n-1本来就存活，n-2天的动物会繁殖，也就是会有2(n-2)+n-1
# def a(n):
#     numList = [1, 1]
#     for i in range(n-2):
#         numList.append(numList[-1]+numList[-2])
#     print numList[-1]
#     return numList

import requests,base64,json
# url="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=bxPo43f8kPUXho0TC01EkiOe&client_secret=Nxo1IcHjKTyBOnOx1z8OKMj0U4embEDa"
# a=requests.get(url)
url2="https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=24.472c0904a54c4c3773eb26f9097347b3.2592000.1528530923.282335-11060237"

def IdentifyingCode(path):
# 二进制方式打开图文件,自定义图片路径
    f = open(path, 'rb')
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    a=requests.post(url2,params=params)
    print (a.content)
    # a=json.loads(a.content)
    # return a['words_result'][0]['words']

IdentifyingCode('/Users/chenfei/desktop/myproject/request_test/22.jpg')
# print a.content