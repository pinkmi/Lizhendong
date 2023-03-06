import pymysql

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Lzd02060223"
}

def add_user(username, password):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "use user"
    cur.execute(sql)
    sql1 = "insert into usersname(username, password) values('%s', '%s')"%(username, password)
    cur.execute(sql1)
    conn.commit()
    conn.close()
    
def is_exist(username, password):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "use user"
    cur.execute(sql)
    sql2 = "select * from usersname where username='%s' and password='%s'"%(username, password)
    cur.execute(sql2)
    res = cur.fetchall()
    if len(res) == 0:
        return False
    else:
        return True