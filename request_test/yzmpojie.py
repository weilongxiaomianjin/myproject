# -*- coding: utf-8 -*-
import json

from PIL import Image
# import ImageEnhance
# import ImageFilter
# import sys


# # 二值化
# threshold = 140
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
#
# def getverify1(name):
#     # 打开图片
#     im = Image.open(name)
#     # 转化到灰度图
#     imgry = im.convert('L')
#     # 保存图像
#     # imgry.save('g' + name)
#     # 二值化，采用阈值分割法，threshold为分割点
#     out = imgry.point(table, '1')
#     out.save('b' + name)
#
#
#
#
# getverify1('2.jpg')  # 注意这里的图片要和此文件在同一个目录，要不就传绝对路径也行



# import pytesseract
# import tesserocr
# image = Image.open('2.png')
# code = tesserocr.image_to_text(image)
# print(code)


import requests ,re
def Method_one():
    """
    识别码出现后调用此函数，保存验证码图片和sig
    返回sig和文件位置去构造新的参数
    :return:
    """
    url='https://mp.weixin.qq.com/mp/verifycode?cert=1526277235094.393'
    headers = {
        'Host': 'mp.weixin.qq.com',
    }
    con=requests.get(url, headers=headers)
    file_path='1.png'
    with open(file_path,'wb')as f:
        f.write(con.content)
    sig=re.findall("sig=([^;]+)",str(con.headers))
    if sig:
        print sig[0]
        return sig[0],file_path
    else:
        print ('none')


import http.client, mimetypes, urllib, json, time, requests

class YDMHttp:
    """
    打码平台调用类
    """
    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb');
        res = requests.post(url, files=files, data=fields)
        return res.text

def shibie(file_path):
    """
    调用打码平台，返回验证码信息
    :param file_path:
    :return:
    """
    # 用户名
    username = 'chen_fi'
    # 密码
    password = '3237830cf'
    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 1
    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '22cc5376925e9387a23cf797cb9ba745'
    # 图片文件
    filename = file_path
    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = 1004
    # 超时时间，秒
    timeout = 60
    # 初始化
    yundama = YDMHttp(username, password, appid, appkey)
    # 登陆云打码
    uid = yundama.login();
    print('uid: %s' % uid)
    # 查询余额
    balance = yundama.balance();
    print('balance: %s' % balance)
    # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
    cid, result = yundama.decode(filename, codetype, timeout);
    print('cid: %s, result: %s' % (cid, result))
    return result

def post_yanzheng():
    """
    获取验证码文件位置和sig，构造新的cookie和请求头发送post请求去破解验证码
    :return:
    """
    sig,file_path=Method_one()
    yzm=shibie(file_path)
    headers = {
        'Host': 'mp.weixin.qq.com',
        'Referer':'https://mp.weixin.qq.com/profile?src=3&timestamp=1526277220&ver=1&signature=mRUtkUSD6JoL9Q7BjFM4u92aiXzK2xtmJ7YF5kcno18aYg1uxJnkxjXNN0rtJEfECizroW6DW3-71NuYJvRgpw==',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Cookie':'pgv_pvid=587974624; tvfe_boss_uuid=fc2366cb08736cdb; _ga=GA1.2.728250831.1516261896; RK=vR70TwZBWc; ptcz=716e3b4c59d9dbca69a8de7540312f5ff495116d3398a84f8734309a3a23ee0d; pgv_pvi=1663131648; pac_uid=1_434890974; o_cookie=434890974; pt2gguin=o0434890974; ua_id=WKoM1mtjm6fvxUT3AAAAAP0pZf0HgL23jZ_gkv-57eU=; mm_lang=zh_CN; noticeLoginFlag=1; remember_acct=434890974%40qq.com; ts_uid=1968319970; xid=cefa2e142d9fd87700117aa29ac13b2f; openid2ticket_o9rvTv5uJRHq8KqmD23N7lzTP2rM=y14dpAfNvS7rGZWfmoSQ6R7uMyH/B3ovSGgThJf+eUY=; '
                 'sig={}'.format(sig)
    }
    data={
        'cert':'1526285741077.1055',
        'appmsg_token':'',
        'input':'{}'.format(yzm)
    }
    ret=requests.post(url='https://mp.weixin.qq.com/mp/verifycode',headers=headers,data=data)
    print ret.content

post_yanzheng()