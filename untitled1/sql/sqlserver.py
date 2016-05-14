# -*- coding: utf-8 -*-
#常见错误in __init__super(Connection, self).__init__(*args, **kwargs2)
#_mysql_exceptions.OperationalError: (1045, "Access denied for user 'ODBC'@'localhost' (using password: YES)")用户名的默认值是本机地址。
import MySQLdb
import hashlib
conn = MySQLdb.Connect(
    host = "127.0.0.1",
    port = 3306,
    user = "biao",
    passwd = "314125",
    db = "user",
    charset = 'utf8'
)
cursor = conn.cursor()
sql = "select passwd from person"
print cursor
cursor.execute(sql)
rs = cursor.fetchall()
print rs
str = '1234'
m = hashlib.md5()
m.update(str)
psw = m.hexdigest()
print psw
print rs==psw
cursor.close()
conn.close()