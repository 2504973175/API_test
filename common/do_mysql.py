import mysql.connector
class DoMydql:
    def do_mysql(self,query,state='all'):
        #需要安装pymysql
        config={
             'host':'',
             'user':'',
             'password':'',
             'port':'',
             'database':''
             }
        #创建数据库连接
        #复习关键字参数
        cnn=mysql.connector.connect(**config)
        cursor=cnn.cursor()
        query_sql='select * from where'
        cursor.execute(query_sql)
        #获取结果打印结果
        if state==1:
            res=cursor.fetchone()
        else:
            res=cursor.fetchall()

        #关闭游标
        cursor.close()
        #关闭连接
        cnn.close()
        return res
if __name__ == '__main__':
    query_sql='select'
    res=DoMydql().do_mysql(query_sql)
    print(res)
    print(res[0][0])