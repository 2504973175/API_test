#操作数据库的方法
#方法没错，需要看下另一台电脑sqlite的位置。
import sqlite3
from config.ProjectConfig import ETConfig
def execute_db(sql):
    conn = sqlite3.connect("D:\\MyDjango\\django_restful\\db.sqlite3")
    cursor=conn.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return result
def init_db():
    execute_db("delete from departments;")
    print("数据库数据已清空")
    # result=execute_db("select * from sqlite_sequence;")
    # print(result)

if __name__ == '__main__':
    init_db()
