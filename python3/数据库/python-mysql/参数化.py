import pymysql
conn = pymysql.connect(host='123.207.68.28', port=3306, user='root' , password='lik', database='test')
cursor = conn.cursor()
sname = input('请输入学生姓名')
sql = 'insert into t1 values(%s,%s)'
# sql = "use test;insert into t1 values(0,'qqq')"


try:
# cursor.execute(sql)
    cursor.execute(sql, ('0',sname))
    conn.commit()
except:
    print('error')
    conn.rollback()
finally:
    cursor.close()
    conn.close()



