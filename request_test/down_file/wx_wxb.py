# -*- coding: utf-8 -*-
import requests
import json
import sys
import copy
import xlwt as xlwt
from lxml import etree
import time , random

reload(sys)
sys.setdefaultencoding('utf8')

def save_excel(lis):
    # 持久化
    f = xlwt.Workbook(encoding='utf-8')
    sheet01 = f.add_sheet(u'微信公众号信息表', cell_overwrite_ok=True)
    # 写标题
    sheet01.write(0, 0, '微信公众号')
    sheet01.write(0, 1, '公众号名')
    sheet01.write(0, 2, '标题')
    sheet01.write(0, 3, '阅读数')
    sheet01.write(0, 4, '点赞数')
    sheet01.write(0, 5, '链接')
    sheet01.write(0, 6, '发布时间')
    sheet01.write(0, 7, '爬取时间')

    # 写内容
    for i in range(len(lis)):
        print(i)
        sheet01.write(i + 1, 0, lis[i].get('source'))
        sheet01.write(i + 1, 1, lis[i].get('author'))
        sheet01.write(i + 1, 2, lis[i].get('title'))
        sheet01.write(i + 1, 3, lis[i].get('reads'))
        sheet01.write(i + 1, 4, lis[i].get('likes'))
        sheet01.write(i + 1, 5, lis[i].get('url'))
        sheet01.write(i + 1, 6, lis[i].get('publish_time'))
        sheet01.write(i + 1, 7, lis[i].get('crawled_time'))

        # 保存
        f.save(u'微信公众号信息表.xls')


headers = {
    # "x-requested-with":"XMLHttpRequest",
    # "referer": "https://data.wxb.com/details/postRead?id=gh_363b924965e9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    "cookie":'visit-wxb-id=a7fd693a15e5513cdebc74cd75c5421f; PHPSESSID=gjbaama340nfsvmh3bdvjdddi0; wxb_fp_id=192344903; Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1524190779,1525316551,1525760967; Hm_lpvt_5859c7e2fd49a1739a0b0f5a28532d91=1526374687'
}
headers2 = {
    "x-requested-with":"XMLHttpRequest",
    "referer": "https://data.wxb.com/details/postRead?id=gh_363b924965e9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    "cookie":'visit-wxb-id=a7fd693a15e5513cdebc74cd75c5421f; PHPSESSID=gjbaama340nfsvmh3bdvjdddi0; wxb_fp_id=192344903; Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1524190779,1525316551,1525760967; Hm_lpvt_5859c7e2fd49a1739a0b0f5a28532d91=1526374687'}

info_list=[]
def parse_detail1(page,id,item):
    #解析第二页到最后一页的函数
    for u in range(2, int(page) + 1):
    # for u in range(2,3):
        print (u,"******************",id)
        json_url = "https://data.wxb.com/account/statArticles/{}?period=30&page={}&sort=".format(id,u)
        time.sleep(random.uniform(5, 8))
        json_data = requests.get(json_url, headers=headers2)
        json_data = json_data.content.decode('utf-8')
        list_info = json.loads(json_data)
        try:
            for o in range(len(list_info['data'])):
                item = copy.deepcopy(item)
                item["publish_time"] = list_info['data'][o]['push_date']
                item["reads"] = list_info['data'][o]['read_num']
                item["title"] = list_info['data'][o]['title']
                item["likes"] = list_info['data'][o]['like_num']
                item["url"] = list_info['data'][o]['url']
                item["crawled_time"] = time.strftime("%Y-%m-%d %X", time.localtime())
                info_list.append(item)
        except:
            pass
            # with open("info.txt", 'a')as f:
            #     f.write(json.dumps(item, indent=2, ensure_ascii=False))

def parse_list(new_url,item,i):
    #解析每一个公众号的第一页，需要传递url
    print (new_url,">>>>>>>>>>>>>>>>>>>>>>>>")
    con=requests.get(new_url,headers=headers)
    new_html=etree.HTML(con.content)
    url_list=new_html.xpath("//tbody[@class='ant-table-tbody']/tr")
    try:
        page = new_html.xpath("//ul[contains(@class,'ant-table-pagination')]/li[last()-1]/a/text()")[0]

        if page:
            for o in url_list:
                item = copy.deepcopy(item)
                item["title"]=o.xpath("./td[1]//a/text()")[0]
                item["url"]=o.xpath("./td[1]//a/@href")[0]
                item["publish_time"]=o.xpath("./td[2]/text()")[0]
                item["reads"]=o.xpath("./td[4]/text()")[0]
                item["likes"]=o.xpath("./td[5]/text()")[0]
                item["crawled_time"] = time.strftime("%Y-%m-%d %X", time.localtime())
                info_list.append(item)
                # with open("info.txt",'a')as f:
                #     f.write(json.dumps(item,indent=2,ensure_ascii=False))
            if "id" in i:
                id=i.split("id=")[-1]
            else:
                id=i
            if int(page)>1:
                #调用解析列表下一页的函数
                parse_detail1(page,id,item)
    except:
        pass

def main():
    item = {}
    time_tamp = int(time.strftime('%d')) - 1
    item["source"] = '公众号'
    item["comments"] = ''
    item["replys"] = ''
    item["repeats"] = ''
    item["likes_ratio"] = ''  # TODO  如果满足条件二，需要计算
    item["fluctuate_ratio"] = ''
    item["hot_ratio"] = ''
    item["explosion_ratio"] = ''
    item["qualified_name"] = ''
    item["qualified_content"] = ''
    item["qualified_time"] = ''
    item["expand_1"] = ''
    item["expand_2"] = ''
    url = "https://data.wxb.com/rank?category=15&page=1"
    a = requests.get(url, headers=headers)
    html = etree.HTML(a.content)
    list = html.xpath("//tbody[@class='ant-table-tbody']/tr/td[2]//div[@class='wxb-avatar-name']/a/@href")
    author_list=html.xpath("//tbody[@class='ant-table-tbody']/tr/td[2]//div[@class='wxb-avatar-name']/a/text()")
    print ("程序开始")

    for i in list: #调用列表解析函数，去解析当前公众号列表的第一页
        new_url = "https://data.wxb.com" + i
        item["author"] = author_list[list.index(i)]
        time.sleep(random.uniform(5, 8))
        parse_list(new_url,item,i)
    #
    # for i in range(2, 5):
    #     print ("公众号列表第{}页解析开始".format(i))
    #     url = "https://data.wxb.com/rank/day/2018-05-{}/15?sort=&page={}&page_size=20".format(time_tamp,i) #TODO 日期需要修改
    #     rank_data = requests.get(url, headers=headers2)
    #     time.sleep(random.uniform(5, 8))
    #     json_data = rank_data.content.decode('utf-8')
    #     list_info = json.loads(json_data)
    #     for o in range(len(list_info)):
    #         item["author"] = list_info['data'][o]['name']
    #         id = list_info['data'][o]['wx_origin_id']
    #         next_url="https://data.wxb.com/details/postRead?id={}".format(id)
    #         time.sleep(random.uniform(5, 8))
    #         parse_list(next_url,item,id)

    save_excel(info_list)
    # print info_list


if __name__ == '__main__':
    main()

# save_excel(lis)

