from MysqlPackage import MysqlPackage
import hashlib
host = '123.207.68.28'
port = 3306
user = 'root'
password = 'lik'
database = 'test'

user_name = input('请输入用户名\n')
user_password = input('请输入密码\n')

user_password = bytes(user_password, 'ascii')
sha1 = hashlib.sha1()
sha1.update(user_password)
sha1_string = sha1.hexdigest()

mp = MysqlPackage(host, port, user, password, database)

try:
    columns = mp.get_one("select * from userinfos WHERE uname=%s",(user_name,))
    print(columns)
except Exception as e:
    print(e)

if columns != None:

    if columns[2] == sha1_string:
        print('success')

