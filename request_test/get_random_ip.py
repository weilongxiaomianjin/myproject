import re
from lxml import etree
import requests

def get_ip():
    # url="http://pvt.daxiangdaili.com/ip/?tid=558965873960293&num=1&filter=on&protocol=https&delay=1"
    url="http://pvt.daxiangdaili.com/ip/?tid=558965873960293&num=100"

    rep = requests.get(url)
    rep = etree.HTML(rep.content)
    ip = rep.xpath("//body//text()")[0]
    print(ip)
    return ip

get_ip()