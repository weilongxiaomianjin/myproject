# -*- coding:utf-8 -*-
import re
import requests
import happybase
import time
from PIL import Image
import redis
import demjson
from pip._vendor.retrying import retry
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import gevent
REDIS_URL = 'redis://newsuser:nFP1$w0zrL7v@10.100.130.1:6379'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
}


class Down_info(object):
    def __init__(self):
        self.cli = redis.from_url(REDIS_URL)
        self.path_video = "/Users/chenfei/desktop/ceshi/vid/"  # TODO 上传前修改
        self.path_pic = "/Users/chenfei/desktop/ceshi/pic/"  # TODO 上传前修改
        self.path_smpic = "/Users/chenfei/desktop/ceshi/smpic/"  # TODO 上传前修改

    def get_redis(self):
        a = self.cli.lpop("tengxun:items")  # TODO 表名待定
        if len(a) > 10:  # 返回字典
            # return demjson.decode(a.decode())
            return eval(a)

    def save_2_redis(self, item):
        self.cli.lpush("txexcpt", item)

    def get_excpt_redis(self):
        a = self.cli.lpop("txexcpt")  # TODO 表名待定
        if len(a) > 30:  # 返回字典
            return demjson.decode(a.decode())

    def save_video_file(self, con, url):
        path = self.path_video + url.split("/")[-1][:10] + str(int(time.time())) + ".mp4"
        with open(path, "wb")as f:
            f.write(con)
        return path

    def save_pic(self, con, url):
        if "gif" in url:
            path = self.path_pic + url.split("/")[-2][-8:] + str(int(time.time())) + ".gif"
        else:
            path = self.path_pic + url.split("/")[-2][-8:] + str(int(time.time())) + ".jpg"
        with open(path, "wb")as f:
            f.write(con)
        return path, url

    def save_small_pic(self, url):
        im = Image.open(url)
        if im.mode != "RGB":
            im = im.convert("RGB")
        height = int(im.size[1] * 350 / im.size[0])
        im.resize((350, height))
        im.thumbnail((350, height))
        path = self.path_smpic + url.split(".jpg")[0].split("/")[-1] + ".jpg"
        im.save(path)
        return path

    def get_redis_num(self, table):
        temp_num = self.cli.llen(table)
        return temp_num


class Handle(object):
    def __init__(self):
        self.connection = happybase.Connection(host="192.168.106.129", port=9090)
        self.table = self.connection.table(b'lasttest5')  # TODO 上传前修改
        self.do = Down_info()

    @retry(stop_max_attempt_number=3)
    def down_file(self):
        item = self.do.get_redis()  # 返回字典格式的数据
        if len(item["videoAddr"])>0 or len(item["imageAddr"])>0:
            try:
                video_info = item["videoAddr"]
                pic_info = item["imageAddr"].split(",")
                sm_pic = item["smallImgCounts"]
                if video_info:
                    con = requests.get(video_info, headers=headers, verify=False, timeout=5)
                    if con.status_code == 200:  # 如果请求成功
                        video_path = self.do.save_video_file(con.content, video_info)
                        item["videoAddr"] = video_path  # 保存视频，更改路径
                        if pic_info:
                            temp_path = ""
                            for i in pic_info:
                                con = requests.get(i, headers=headers, verify=False, timeout=5)
                                path, url = self.do.save_pic(con.content, i)
                                temp_path += path + ","
                                item["content"] = re.sub(i, path, item["content"])
                            item["content"] = "<video src='" + video_path + "'></video>" + item["content"]
                            item["content"] = item["content"].strip('"')
                            item["imageAddr"] = temp_path[:-1]
                            temp_path = ""
                            small_pic_list = item["imageAddr"].split(",")
                            for i in range(sm_pic):
                                url = small_pic_list[i]
                                path = self.do.save_small_pic(url)
                                temp_path += path + ","
                            item["smallImgAddr"] = temp_path[:-1]
                            return item
                        else:
                            return item
                else:
                    temp_path = ""
                    for i in pic_info:
                        con = requests.get(i, headers=headers, verify=False, timeout=5)
                        path, url = self.do.save_pic(con.content, i)
                        temp_path += path + ","
                        item["content"] = re.sub(i, path, item["content"])
                    item["imageAddr"] = temp_path[:-1]
                    temp_path = ""
                    small_pic_list = item["imageAddr"].split(",")
                    for i in range(sm_pic):
                        url = small_pic_list[i]
                        path = self.do.save_small_pic(url)
                        temp_path += path + ","
                    item["smallImgAddr"] = temp_path[:-1]
                    return item
                print(item["title"])
            except Exception as ret:
                pass
        else:
            return item

    def handle_excpt(self, item):
        try:
            if item:
                new_item = {("cf:" + str(i[0])).encode("utf-8"): str(i[1]).encode("utf-8") for i in item.items() if
                            i[0] != "id"}
                self.table.put(item["id"].encode("utf-8"), data=new_item)
                self.table.batch().send()
                return 200
            else:
                pass

        except Exception as ret:
            self.do.save_2_redis(item)

    def down_excpt(self):
        item = self.do.get_excpt_redis()
        if item:
            self.handle_excpt(item)


def down_insert_hbase():
    a = Handle()
    item = a.down_file()
    a.handle_excpt(item)

# down_insert_hbase()

def retry_down():
    temp_c = Handle()
    while True:
        i = temp_c.do.get_redis_num("tengxun:items")
        if i > 0:
            g1 = gevent.spawn(down_insert_hbase)
            g2 = gevent.spawn(down_insert_hbase)
            g3 = gevent.spawn(down_insert_hbase)
            g4 = gevent.spawn(down_insert_hbase)
            g5 = gevent.spawn(down_insert_hbase)
            g1.join()
            g2.join()
            g3.join()
            g4.join()
            g5.join()

        else:
            print("download--over")
            break


retry_down()
