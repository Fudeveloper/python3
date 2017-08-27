import pymysql
# print(dir(pymysql))
# help(pymysql.connect)
conn = pymysql.connect(host='123.207.68.28', port=3306, user='root' , password='lik', database='test')

cursor = conn.cursor()
try:
    columns = cursor.execute('select * from student')
    # for i in cursor.fetchall():
#     print(i)
    for i in range(columns):
        print(cursor.fetchone())
except Exception as e:
    print(e)
cursor.close()
conn.close()
