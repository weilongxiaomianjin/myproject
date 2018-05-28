import re
from lxml import etree
import requests

class Get_ip():
    def __init__(self):
        self.url = "http://pvt.daxiangdaili.com/ip/?tid=558965873960293&num=1&filter=on&protocol=https&delay=1"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
        }
        self.test_url = "http://www.ip111.cn/"

    def get_info(self):
        rep = requests.get(self.url)
        rep = etree.HTML(rep.content)
        ip = rep.xpath("//body//text()")[0]
        return ip

    def test_ip(self, ip):
        rep = requests.get('http://www.ip111.cn/', headers=self.headers, proxies={"http": "http://{}".format(ip)})
        rep = etree.HTML(rep.content)
        ip_adr = rep.xpath("//tr[2]/td[2]/text()")[0]
        ip_adr = ".".join(re.findall(r"\d+", ip_adr, re.S))
        new_ip=ip.split(":")[0]
        if ip_adr == new_ip:
            return ip
        else:
            print("ip获取异常")

    def run(self):
        ip = self.get_info()
        test_ip = self.test_ip(ip)
        print(test_ip)
        return test_ip


if __name__ == '__main__':
    get_ip = Get_ip()
    get_ip.run()
