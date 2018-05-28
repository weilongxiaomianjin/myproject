# -*- coding: utf-8 -*-
import copy
import csv
import hashlib
import json
import re
import time, random
from user_agent import randomm

import requests
ipp=''

headers = {  # 手机请求头
    'Host': 'weixin.sogou.com',
    'User-Agent': randomm()
}
headers2={
    'Host': 'mp.weixin.qq.com',
    'User-Agent':randomm(),
    'Cookie':'rewardsn=; wxtokenkey=777',
}

def parse_url(url2,item):
    # ipp = requests.get("http://192.168.122.105:5000/weixin/1/").text
    # print (ipp)
    # global ipp
    # ip = {"http": "http://{}".format(ipp)}
    con=requests.get(url2,headers=headers2)
    con=con.content
    print con
    url_list = re.findall('content_url":"([^"]+)', con)
    title_list = re.findall('"title":"([^"]+)', con)
    for i in url_list:
        item = copy.deepcopy(item)
        i = i.replace('amp;', '')
        item['url'] = i
        item['title'] = title_list[url_list.index(i)]
        print(item)
        # with open("wx.txt", "a")as f:
        #     f.write(item)
        #     f.write("\n")

def parse_list():
    for i in [
        '冷兔',
        #'小林', '六神磊磊读金庸', '豆瓣', '不正常人类研究中心', '胡辛束', '张佳玮写字的地方', '环球人物', '曹植', '姜茶茶', '文馆', '末那大叔', '国馆',
        # '虎扑体育', '一条', '设计最前沿', 'HYPEBEAST', '知日', '乌鸦电影', '淘漉音乐', '美芽', '凯叔讲故事', '灼见', '青塔', '开始吧', '篮球新说', '王左中右',
        # '柯首映', '铲史官', '黎贝卡的异想世界', '才华有限青年', '人民日报', '异能八卦局', '美少女挖掘机', '书法思考', '少年怒马', '艾格吃饱了', '杭州本地宝', '篮球湿叔',
        # '人物', '思想聚焦', '视觉志', '深焦DeepFocus', '归零归零', '拾遗', '腾讯体育', '萝严肃', '混子曰', '拜托了老斯基', '行周末', '搜狐体育', '几何民宿',
        # '看理想', 'CITYZINE', '王尼玛', '苏群', '混子谈钱', '备胎说车', '人间旅行指南', '行动派DreamList', 'Before after', '桃红梨白', '活法儿',
        # '年糕妈妈', 'InstaFit', '语言学午餐Ling-Lunch', '南方周末', 'ONE文艺生活', '冯站长之家', '罗严肃', '有束光', '新华社', '摇滚客', '插座学院',
        # '虎嗅网', '日本那些事', '果壳网', '36氪', '新浪体育', '今日话题', 'BWC中文网', '吴晓波频道', '网易新闻', '十点读书', '王猛', '泽平宏观', 'sir电影',
        # '菜菜美食日记', '阿何有话说', '经济日报', '职场充电宝', '山石观市', 'AutoLab', '为你写一个故事', '东东和西西', '新世相', '罗辑思维', '书单来了', '宝宝辅食微课堂',
        # '听明明吹牛皮', '地球知识局', '澎湃新闻', '侠客岛', '好好虚度时光', '菲凡说', 'BB姬', '美食台', '石榴婆报告', '经管之家', '黄小姐蓝小姐', '青音约', '深夜发媸',
        # '混沌大学', '第一财经资讯', '足球之路', '请不要害羞', '灵魂有香气的女子', 'Voicer', '搜达足球', '咪蒙', '蕊希'
    ]:
        # ipp=requests.get("http://192.168.122.105:5000/weixin/1/").text
        # print (ipp)
        # global ipp
        # ip = {"http": "http://{}".format(ipp)}
        url = "http://weixin.sogou.com/weixinwap?query={}&type=1&ie=utf8&_sug_=n&_sug_type_=&s_from=input".format(i)
        time.sleep(random.uniform(2,5))
        con=requests.get(url,headers=headers)

        if "验证码" not in con.content:
            tamp="".join(re.findall('timestamp=([^&]+)',con.content))
            sig="".join(re.findall('ignature=([^=]+)',con.content))
            sig=sig+"=="
            #获取到这个公众号的URL（构造出）
            item={}
            item['source']='公众号'
            item['author']=i
            # 最新的文章信息  返回一堆最近两三天发布的文章内容，再构造url
            url2="http://mp.weixin.qq.com/profile?src=3&timestamp={}&ver=1&signature={}".format(tamp,sig)
            time.sleep(random.uniform(2,5))
            print url2
            parse_url(url2,item)
        else:
            print ("ip is done........")
            break

parse_list()



            # f_url="http://mp.weixin.qq.com/s?timestamp=1524188275&src=3&ver=1&signature=2rvllKscGxaZA-aJGVRrxnGGWEPgDfbCK-0M8T7FzaW7LDxd1dRYCcVbriSBGzk6eEDDBTGuJeb5fWXaIYB5WZMNzJc77XWSCHsJ4iVCWrBtOuxANnVIFIjRot4w9eZPi1HmYgcyhnzux7lSS*2Vn7rBfAoqVLiBq*i3HR3JI90="

#获取最终的文章链接 需要去掉3个amp
# f_url="https://mp.weixin.qq.com/s?src=11&timestamp=1524190566&ver=827&signature=rFyqfk9u16lBThzkOjX1lv*df*-VkZW6mmkaudIB6UxjF7rkGmlm3Kr0adLym8z7ZfGBLfSeKY85UWP3zsPNMJEs59pPIRYwalamGeBQeu13DUaekZf-dJLKw8jj8v0v&new=1"
# c=requests.get(f_url,headers=headers2,allow_redirects=True)
# print c.content

