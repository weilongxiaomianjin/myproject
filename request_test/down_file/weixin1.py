# import requests
# url="http://localhost:8050/render.html?url=http://www.cyzone.cn/category/8/"
# response=requests.get(url)
# print response.content
import demjson
a_c="{a:1,b:'2'}"
a=demjson.decode(a_c)
print a["a"]