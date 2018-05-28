# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import time
# 请求函数
def getpage(keys):
    # 创建一个浏览器对象
    browser = webdriver.Chrome()
    # 使用浏览器对象进行目标站点的访问
    browser.get('https://s.taobao.com/search?q={}'.format(keys))
    time.sleep(2) #等待2秒
    # 获取html
    html = browser.page_source
    # 调用解析函数，传入所获取的目标站点的response
    listpage(html,keys)
    # 点击下一页,共一百页
    for num in range(100):
        browser.find_element_by_class_name('next').click()
        time.sleep(3)
        html = browser.page_source
        listpage(html,keys)
        # 点到最后一页停止
        if 'next-disabled' in browser.page_source:
            browser.close()
            break
# 解析函数
def listpage(html,keys):
    print("正在解析页面")
    #把传入的信息进行处理，变为能够被选择器使用的对象
    html = BeautifulSoup(html,'lxml')
    #使用选择器选取出符合规则的所有信息，组成一个列表
    shop_list = html.select('div.ctx-box')
    with open(keys+".txt", 'a') as f:
        excel_list = []
        for i in shop_list:
            #遍历这个列表，选出每一个单独的商品信息进行提取
            money = i.select('div.price')[0].text.strip() #价格
            num = i.select('div.deal-cnt')[0].text        #付款人数
            goods = i.select('a.J_ClickStat')[0].text.strip()  #商品信息
            shopname = i.select('a.shopname span')[-1].text   #店铺名
            print(shopname)
            address = i.select('div.location')[0].text  #店铺地址
            excel_list.append(','.join([money, num, goods, shopname, address])+'\n')
        f.writelines(excel_list)

if __name__ == '__main__':
    keys = '汽车玩具'
    getpage(keys)

