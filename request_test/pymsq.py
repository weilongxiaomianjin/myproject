# -*- coding: utf-8 -*-
# import sys
from pymysql import *
# reload(sys)
# sys.setdefaultencoding('utf8')

def main():
    # 创建链接
    con = connect(host='127.0.0.1', port=3306, database='fenghuang', user='root', password='cfmysql', charset='utf8')
    # 创建指针
    cs = con.cursor()
    # re_msg=cs.execute("select * from goods_cates;")
    # for i in range(re_msg):
    #     print(cs.fetchone())
    # 指针操作sql语句--插入      表名称    列名1,2,3         内容1,2,3
    # cs.execute("""insert into hot_spot(title,url,comments) VALUES("新闻1","www.baidu.com","123");""")
    # 修改
    # cs.execute("""update hot_spot set title='新闻2',url='www.xina.com',comments='321';""")
    # 删除
    # cs.execute("""delete from hot_spot where id=1;""")
    # 提交操作
    # con.commit()
    # 查询操作
    re_msg = cs.execute("select * from hot_spot;")
    for i in range(re_msg):
        print(cs.fetchone())
    # 关闭指针
    cs.close()
    # 关闭连接
    con.close()


if __name__ == "__main__":
    main()
