#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: cling
import json
import random
import re

import requests
import time

#
# def get_num(item):
#     """获取阅读量和点赞数量"""
#     headers = {  # 手机请求头
#         'Host': 'mp.weixin.qq.com',
#         'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
#         "Cookie": "Cookie: rewardsn=; wxtokenkey=777; wxuin=2923743027; devicetype=Windows10; version=6206021b; lang=zh_CN; pass_ticket=PeyDM6nFBt7Cr6VNTXFC8PJjf98SPJFTGK85gwkssLhGFP0N2dGBnTnfWhKgCE2Y; wap_sid2=CLOOk/IKElx2QVAyajk4aVllUXAyQ2Y4TXZtV2dTUVg3WHBfYjNubVZMYmNqekh0OUNBMXJ0eVNMWDJraVpmM3p5Wkg0N3Yyc3drNEJtV2VlR3poc0NFOWpLMnJLcmdEQUFBfjDNmdbWBTgNQAE=",
#     }
#     appmsg_token='952_bQvRNwz81Fck48fiVTHJnSXnQsFmpa-GvKTCLcLYCPHW-Enl72JoV_F1UhRuq65FD3MZslXNI__BU3m1'
#     # appmsg_token='952_w5dyLqZ1LoxoXpA42oO3l30LtcWwWBYY5qtKPGiLjSNa1lC0fAtlhCr1EVfrEQwhrvUFJicDHX17LzoD'
#     biz = re.findall(r'__biz=(.*?)&', item["url"])[0]
#     mid = re.findall(r'mid=(.*?)&', item["url"])[0]
#     sn = re.findall(r'sn=(.*?)&', item["url"])[0]
#     idx = re.findall(r'idx=(.*?)&', item["url"])[0]
#     params = {
#         "__biz": biz,  # 唯一公众号识别信息
#         "mid": mid,  #
#         "sn": sn,  #
#         "idx": idx,  #
#     }
#     data = {
#         "is_only_read": "1",  # 不要就没有阅读数量信息
#     }
#     # 通过电脑客户端
#     url = 'https://mp.weixin.qq.com/mp/getappmsgext?appmsg_token={}'.format(appmsg_token)
#     content = requests.post(url, headers=headers, data=data, params=params).json()
#     item["reads"] = content["appmsgstat"]["read_num"]
#     item["likes"] = content["appmsgstat"]["like_num"]
#     print("阅读数:%s,点赞数:%s" % (item["reads"], item["likes"]))
#     print(222, item)
#     with open('weixin.txt', 'a') as f:
#         json.dump(item, f, ensure_ascii=False)
#     time.sleep(random.uniform(4, 8))
#
#
# def get_info(fakeid):
#     """通过公众平台订阅号获取微信artcle信息"""
#     headers = {
#         'origin':'https://mp.weixin.qq.com',
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#         "Cookie": 'Cookie: sd_userid=39011523674991825; sd_cookie_crttime=1523674991825; pgv_pvid=8464447224; pgv_info=ssid=s4566395272; rewardsn=; wxtokenkey=777; wxuin=2923743027; devicetype=android-26; version=26060536; lang=zh_CN; pass_ticket=b+/EQOtDd6g37ysiASVqZEqxcKfxzdx9p3i9VgDbnPkVO/NUzfrx/V3OzTHeDIPK; wap_sid2=CLOOk/IKEnBGOUdhUTgyRHRnQk5ncl9ETzJ4QVhxSXhINElFZG9TQ255Z2VOblRVZUktUWdQb1dDRHdyZ1hpMVlvTHhEcF8tRG5tYXNQX2lVcXp2ZGhNMGV6UWNGelBfb0ZZQl9zbjd1U3N1aF84b2dNQzRBd0FBMIKm1tYFOA1AAQ==',
#     }
    # 登录生成token密令,page起始页从0开始,每次增加5页,fakeid对应公众号唯一识别码
    # for page in range(0, 5, 5):
    #     url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?token={}&lang=zh_CN&f=json&ajax=1&random=0.814385758031624&action=list_ex&begin={}&count=5&query=&fakeid={}&type=9'.format(token, page, fakeid)
    # url = 'https://mp.weixin.qq.com/mp/getappmsgext?f=json&uin=777&key=777&pass_ticket=b%25252B%25252FEQOtDd6g37ysiASVqZEqxcKfxzdx9p3i9VgDbnPkVO%25252FNUzfrx%25252FV3OzTHeDIPK&wxtoken=777&devicetype=android-26&clientversion=26060536&appmsg_token=952_RunsbdPhJSk6M9KzVTHJnSXnQsFmpa-GvKTCLe-2WG94hLEp9FcxgDX8vy15qmQ_m3LpWlJWQnS9hGtO&x5=1&f=json'
    # 使用get方法进行提交#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: cling
import json
import random
import re

import requests
import time

#
# def get_num(item):
#     """获取阅读量和点赞数量"""
#     headers = {  # 手机请求头
#         'Host': 'mp.weixin.qq.com',
#         'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
#         "Cookie": "Cookie: sd_userid=39011523674991825; sd_cookie_crttime=1523674991825; pgv_pvid=8464447224; pgv_info=ssid=s4566395272; rewardsn=; wxtokenkey=777; wxuin=2923743027; devicetype=android-26; version=26060536; lang=zh_CN; pass_ticket=b+/EQOtDd6g37ysiASVqZEqxcKfxzdx9p3i9VgDbnPkVO/NUzfrx/V3OzTHeDIPK; wap_sid2=CLOOk/IKEnBGOUdhUTgyRHRnQk5ncl9ETzJ4QVhxSXhINElFZG9TQ255Z2VOblRVZUktUWdQb1dDRHdyZ1hpMVlvTHhEcF8tRG5tYXNQX2lVcXp2ZGhNMGV6UWNGelBfb0ZZQl9zbjd1U3N1aF84b2dNQzRBd0FBMIKm1tYFOA1AAQ==",
#     }
#     appmsg_token='952_bQvRNwz81Fck48fiVTHJnSXnQsFmpa-GvKTCLcLYCPHW-Enl72JoV_F1UhRuq65FD3MZslXNI__BU3m1'
#     # appmsg_token='952_w5dyLqZ1LoxoXpA42oO3l30LtcWwWBYY5qtKPGiLjSNa1lC0fAtlhCr1EVfrEQwhrvUFJicDHX17LzoD'
#     biz = re.findall(r'__biz=(.*?)&', item["url"])[0]
#     mid = re.findall(r'mid=(.*?)&', item["url"])[0]
#     sn = re.findall(r'sn=(.*?)&', item["url"])[0]
#     idx = re.findall(r'idx=(.*?)&', item["url"])[0]
#     params = {
#         "__biz": biz,  # 唯一公众号识别信息
#         "mid": mid,  #
#         "sn": sn,  #
#         "idx": idx,  #
#     }
#     data = {
#         "is_only_read": "1",  # 不要就没有阅读数量信息
#     }
#     url = 'https://mp.weixin.qq.com/mp/getappmsgext?wxtoken=777&devicetype=android-26&clientversion=26060536&x5=1&f=json&appmsg_token={}'.format(appmsg_token)
#     content = requests.post(url, headers=headers, data=data, params=params).json()
#     item["reads"] = content["appmsgstat"]["read_num"]
#     item["likes"] = content["appmsgstat"]["like_num"]
#     print("阅读数:%s,点赞数:%s" % (item["reads"], item["likes"]))
#     print(222, item)
#     with open('weixin.txt', 'a') as f:
#         json.dump(item, f, ensure_ascii=False)
#     time.sleep(random.uniform(4, 8))


def get_info(fakeid):
    """通过公众平台订阅号获取微信artcle信息"""
    headers = {
        'origin':'https://mp.weixin.qq.com',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        # "Cookie": "noticeLoginFlag=1; pgv_pvi=5230921728; pgv_pvid=3623998610; RK=vUvSotSrGK; ptcz=6cfb7813c401718ffb46717a940675ac7a513d8e6357a669d3669e01378a0873; tvfe_boss_uuid=313892a9d13e6e74; _ga=GA1.2.1134837011.1514882051; mobileUV=1_1610d6e5610_dd18a; fontsize=size_n; pac_uid=1_391506838; sd_userid=10151522720659956; sd_cookie_crttime=1522720659956; ua_id=6iWfkFGqDP91BPQRAAAAAHGmo5Pfno0Bov51RMW49m8=; mm_lang=zh_CN; ptui_loginuin=3247562437; pt2gguin=o3247562437; noticeLoginFlag=1; o_cookie=3247562437; rewardsn=; wxtokenkey=777; pgv_si=s9834433536; ticket_id=gh_027444d499dc; cert=K3F6qrGZy_XGH4cbOHbshbMm8rA6pxZr; pgv_info=ssid=s599186112; uuid=0d2e643a4ee33e2ed84fd2f7213cc55b; ticket=655c0555d306ad810f8076d57cbd2eba279d26bd; data_bizuin=3550795052; bizuin=3540794528; data_ticket=+5zFEdh7LO5U3AHtPn44e+EraX9Fc55HfZfX+7NXF+nI8Z2qqQZh7Zdnwwp/QsRy; slave_sid=dkJINTdyNUxKWkpwdGhNT1VJNmNJNmtCWkRBUmtXNjFCVTRQem9pdE5GUXB1eThwbzZHQTRuQmxpYWI4d2ZIU2RES3RPc0pXeENqZE82WWtwOEE1Uk1uTFNqSFJ3NGtDU1ZlQzdmaHdJZXA3V2hrSnlwSjVsWWxkT0lTQkhRbUFHV3BMWkpVekJWSkY5dzll; slave_user=gh_027444d499dc; xid=a38fce1b4b49b0e7aa062486bcd84c94; openid2ticket_oLNWk02aJu3xTsezL5LOfMiIX3rU=SbSBI/0UHZfVtzvI62AXgY5l5ftpYcUUbVn3tXaa73Y="
    }
    item={}
    # 登录生成token密令,page起始页从0开始,每次增加5页,fakeid对应公众号唯一识别码
    for page in range(0, 5, 5):
        url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?token=467565625&lang=zh_CN&f=json&ajax=1&random=0.814385758031624&action=list_ex&begin={}&count=5&query=&fakeid={}&type=9'.format(page, fakeid)

        # 使用get方法进行提交
        res = requests.get(url, headers=headers)
        resp = json.loads(res.text)
        # 返回了一个json，里面是每一页的数据
        for i in resp["app_msg_list"]:
            # 提取每页文章的标题及对应的url
            item["title"] = i.get("title")
            item["url"] = i.get("link")
            item["publish_time"] = i.get("update_time")
            print(item)
            # get_num(item)


# if __name__ == '__main__':
#     token = '525999572'
#     item = dict()
    # get_info('MjM5Njc0MjIwMA==') # 图灵教育
    # get_info('MzU3MzQ4NzE1OA==') # it派
    # get_info('MTgwNTE3Mjg2MA==') # 冷兔
    # get_info('MjM5MjAxNDM4MA==') # 人民日报
    # for i in ['MjM5Njc0MjIwMA==','MzU3MzQ4NzE1OA==','MTgwNTE3Mjg2MA==']:
    #     get_info(i)

    # res = requests.get(url, headers=headers)
    # resp = json.loads(res.text)
    # 返回了一个json，里面是每一页的数据
    # for i in resp["app_msg_list"]:
        # 提取每页文章的标题及对应的url
        # item["title"] = i.get("title")
        # item["url"] = i.get("link")
        # item["publish_time"] = i.get("update_time")
        # print(item)
        # get_num(item)


# if __name__ == '__main__':
#     token = '525999572'
#     item = dict()
    # get_info('MjM5Njc0MjIwMA==') # 图灵教育
    # get_info('MzU3MzQ4NzE1OA==') # it派
get_info('MTgwNTE3Mjg2MA==') # 冷兔
    # get_info('MjM5MjAxNDM4MA==') # 人民日报
    # for i in ['MjM5Njc0MjIwMA==']:
