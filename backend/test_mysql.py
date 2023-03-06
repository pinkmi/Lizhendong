import pymysql

def mysql_db():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        database="name",
        charset="utf8",
        user="root",
        password="Lzd02060223"
    )
    try:
        with conn.cursor() as cursor:
            sql = "select * from tb2"
            cursor.execute(sql)
            datas = cursor.fetchall()
            print("获取到的数据：\n", datas)
    except Exception as e:
        print("数据库异常操作：\n", e)
    finally:
        conn.close()


if __name__ == "__main__":
    mysql_db()