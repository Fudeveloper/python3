import pymysql
class MysqlPackage(object):
    def __init__(self, host, port, user, password, database,charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    def connect(self):
        # print('--1--')
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
        # print('--2--')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
        self.cursor.close()

    def insert(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params):
        return self.__edit(sql, params=())

    def update(self, sql, params):
        return self.__edit(sql, params=())

    def __edit(self, sql, params=()):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print('{0}\t\tMysqlPackager.py line 28'.format(e))
        return count

    def get_all(self, sql, params=()):
        list = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print('{0}\t\tMysqlPackager.py line 39'.format(e))
        return list

    def get_one(self, sql, params=()):
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
            return result
        except Exception as e:
            print('{0}\t\tMysqlPackager.py line 50'.format(e))



