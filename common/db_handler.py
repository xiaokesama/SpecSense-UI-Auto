import pymysql


class DB:
    def __init__(self, db_config: dict):
        self.conn = pymysql.connect(**db_config)

    def get_one(self,sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()

    def get_many(self,sql,size:int):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchmany(size)

    def get_all(self,sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def exist(self,sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            if cursor.fetchone():
                return True
            else:
                return False

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    import settings
    db = DB(settings.DB_CONFIG)
    print(db.get_one("SELECT * FROM student WHERE id=2"))

