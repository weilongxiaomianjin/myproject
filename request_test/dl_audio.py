# -*- coding:utf-8 -*-
from gevent import monkey;

monkey.patch_socket()
import gevent
import requests
import happybase
import time
from PIL import Image
import redis
import demjson
from pip._vendor.retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
}

REDIS_URL = 'redis://newsuser:nFP1$w0zrL7v@10.100.130.1:6379'


class Down_info(object):
    def __init__(self):
        self.cli = redis.from_url(REDIS_URL)
        self.path_audio = "/data/audio/kaola/"
        self.path_pic = "/data/images/kaola/"  # TODO

    def get_redis(self):
        a = self.cli.lpop("kaola:items")  # TODO 表名待定
        if a:  # 返回字典
            return eval(a)

    def save_2_redis(self, item):
        self.cli.lpush("excpt", item)

    def get_audio_redis(self):
        a = self.cli.rpop("kaola:items")  # TODO 表名待定
        if a:  # 返回字典
            return eval(a)

    def get_excpt_redis(self):
        a = self.cli.lpop("excpt")  # TODO 表名待定
        if len(a) > 10:  # 返回字典
            return demjson.decode(a.decode())

    def get_redis_num(self, table):
        temp_num = self.cli.llen(table)
        return temp_num


    def save_audio_file(self, con, path):
        file_path = self.path_audio + path.split("-")[-1].split(".")[0] + str(
            int(time.time())) + ".mp3"
        with open(file_path, "wb")as f:
            f.write(con)
        return file_path

    def save_audio_pic(self, con, url):
        path = self.path_pic + url.split("/")[-2] + str(int(time.time())) + ".jpg"
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
        path = "" + url.split(".jpg")[0].split("/")[-1] + ".jpg"
        im.save(path)
        return path


class Handle(object):
    def __init__(self):
        self.connection = happybase.Connection(host="hbase.51fbops.com", port=9090)
        self.table = self.connection.table(b'news')
        self.do = Down_info()

    @retry(stop_max_attempt_number=3)
    def down_audio(self):
        item = self.do.get_audio_redis()
        if item:
            try:
                audio_info = item["audioAddr"]
                audio_pic = item["videoPic"]
                if audio_info:
                    con = requests.get(audio_info, headers=headers, verify=False, timeout=5)
                    if con.status_code == 200:
                        item["audioAddr"] = self.do.save_audio_file(con.content, audio_info)
                if audio_pic:
                    con = requests.get(audio_pic, headers=headers, verify=False, timeout=5)
                    if con.status_code == 200:
                        item["videoPic"], url = self.do.save_audio_pic(con.content, audio_pic)
                        item["smallImgAddr"] = item["videoPic"]
                return item
            except Exception as ret:
                self.do.save_2_redis(item)
        else:
            print("音频全部下载完毕")
            return 1

    def handle_excpt(self, item):
        try:
            new_item = {("cf:" + str(i[0])).encode("utf-8"): str(i[1]).encode("utf-8") for i in item.items() if
                        i[0] != "id"}
            a=self.table.row(item["id"])
            if not a:
                self.table.put(item["id"].encode("utf-8"), data=new_item)
                self.table.batch().send()
                print(item["title"])
                return 200
        except Exception as ret:
            self.do.save_2_redis(item)

    def down_excpt(self):
        item = self.do.get_excpt_redis()
        if item:
            print("----------------excpt------------------------")
            self.handle_excpt(item)




def down_insert_hbase():
    a = Handle()
    item = a.down_audio()
    a.handle_excpt(item)


def retry_down():
    for i in range(6):
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


def do_excpt():
    a=Handle()
    for i in range(a.do.get_redis_num("excpt")):
        a.down_excpt()


retry_down()
# do_excpt()