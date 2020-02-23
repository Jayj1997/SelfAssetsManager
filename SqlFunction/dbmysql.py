import pymysql


class sqlManage:
    def __init__(self):
        self.host = '122.51.95.201'
        self.user = 'root'
        self.password = '919169807'
        self.charset = 'UTF8MB4'
        self.port = 3306
        self.db = 'selfAssetsManager'

    def connect(self):
        try:
            con = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                  charset=self.charset, port=self.port, db=self.db)
            cur = con.cursor()
            return con, cur
        except Exception as e:
            print(e)
            return None

    # 增删查改数据的方法
    def execute(self, sql):
        con, cur = self.connect()
        try:
            con.begin()
            cur.execute(sql)
            con.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cur.close()
            con.close()

    def fetchall(self, sql):
        con, cur = self.connect()
        try:
            cur.execute(sql)
            result = cur.fetchall()
            con.commit()
            return result
        except Exception as e:
            print(e)
            return False
        finally:
            cur.close()
            con.close()