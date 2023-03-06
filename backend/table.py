import pymysql

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Lzd02060223"
}

conn = pymysql.connect(**config)

cur = conn.cursor()
sql = ["use user;", "create table usersname(id int auto_increment primary key, username varchar(30) not NULL, password varchar(30) not NULL) default charset=utf8"]
# cur.execute(sql)
for item in sql:
    cur.execute(item)

conn.close()