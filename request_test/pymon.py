from pymongo import *

# insert_one  加一条文档对象
# insert_many 多条
# find_one 查询一条
# find  多条
# update_one  更新一条
# update_many
# delete_one
# delete_many

if __name__ == '__main__':
    try:
        # 创建连接对象
        client = MongoClient(host='localhost', port=27017)
        # 获得数据库，此处使用python数据库
        db = client.python
        # 删除满足条件的第一条文档
        # db.stu.delete_one({'gender':False})
        #对于stu表进行操作
        db.stu.insert_one({"title":"xinwen"})

        # 删除满足条件的所有文档
        # db.stu.delete_many({'gender': True})
        print('ok')
    except Exception as e:
        print (e)