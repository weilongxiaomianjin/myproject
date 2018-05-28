#source activate name 开启虚拟环境
#source deactivate name 关闭虚拟环境

#/usr/local/mysql/bin/mysql -u root -p 开启
#mysql password   cfmysql

#sudo mongod --config /usr/local/etc/mongod.conf 第一个终端开启mongo
#mongo 第二个终端使用

#gtilab chenfei chenfi 563585538@qq.com  3237830cf
#阿里云邮箱 chenfei@edspay.com  1223zwCF

#ssh newsuser@10.100.130.1 -p 10036 连接远程服务器 密码 EV$l86ky
#ssh root@10.100.110.73 -p 10036 连接远程存储服务器 密码 Alading@2017
#ssh root@192.168.115.31 hik12345  跳转


#java -jar

#http://openapi.kuaibao.qq.com/getCityNewsIndex?callback=responseData&cityName=%E6%AD%A6%E6%B1%89&_=1519874148437   腾讯城市新闻接口


# 爬虫存储地址：192.168.115.101   账号：root ，密码: hik12345
# 业务运行地址：192.168.115.102   测试
# redis : 192.168.116.173

# redis-cli -h 192.168.116.173
# AUTH nFP1$w0zrL7v

#scp -P 10037 /Users/chenfei/Desktop/myproject/request_test/py_hbase.py newsuser@183.131.0.134:/home/newsuser/tengxun  上传文件

# mongo -u admin -p ppnn13fish

#http://183.131.0.134:10040/phpmyadmin/index.php
#pachong sLt2FgVJTRQSFXwW

#qq 3247562437

#服务器文件地址 http://image.yf.51fanbei.com/thumb/tengxun/558929201519959242.jpg
#腾讯滚动新闻链接
#http://coral.qq.com/article/news/datetop?format=json&source=1&callback=jQuery112004793799494996991_1514537340846&_=151453734
import time

from selenium.webdriver.support import wait

import get_new_ip

url="https://xw.qq.com/news/20180102013679"


import requests

#解析详情页（包含正文和图片顺序）
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
# a=webdriver.Chrome()

mobileEmulation = {'deviceName': 'iPhone 8 Puls'}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)

a = webdriver.Chrome()


a.implicitly_wait(30)
a.get(url)

b=a.find_element_by_class_name("txp_poster").click()

time.sleep(1)
video_a=a.find_element_by_xpath("//txpdiv[@class='txp_video_container']/video")
src=video_a.get_attribute("src")
print(src)



#评论页面分析
"""在详情页有一个div的class包含fixnav nopad，然后里面的链接指向另一个页面，
页面中有几个接口比如https://coral.qq.com/article/2468874936/comment
其中ID为这篇新闻的ID，返回一组json格式的数据，里面包含所有回复内容content和每条回复的二级回复数量rep，
其中key为replyuser是对上面回复的二级回复
nick 用户名
head头像
up 点赞数
region 地区"""




#单开项目多线程
# def main(offset):
#     url = 'http://maoyan.com/board/4?offset=' + str(offset)
#     html = get_one_page(url)
#     for item in parse_one_page(html):
#         print(item)
#         write_to_file(item)
#
# if __name__ == '__main__':
#     p = Pool()
#     p.map(main,[i*10 for i in range(10)])

































