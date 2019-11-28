import pymysql
import traceback


class MyPymysql(object):
    def __init__(self):
        self.dbinfo = dict(host="127.0.0.1", user="root", password="root", database="pyfei", charset="utf8")

    def __enter__(self):
        try:
            self.conn = pymysql.connect(**self.dbinfo)
            self.cursor = self.conn.cursor()
            return self.cursor
        except Exception as e:
            traceback.print_exc()
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.conn.rollback()
                # 返回False 传播异常
                # 返回True 终止异常 不要这么做
                # 抛出不同的异常 代替 原有异常
                return False
            else:
                self.conn.commit()
        except Exception as e:
            traceback.print_exc()
            raise e
        finally:
            self.cursor.close()
            self.conn.close()
