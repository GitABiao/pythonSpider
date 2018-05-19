#coding=utf-8
import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user='biao',
    passwd='314125',
    db='user',
    charset = "utf8"
)
cur = conn.cursor()
sql = "select * from person"
cur.execute(sql)
for row in cur:
    print "id=%s,name=%s,passwd=%s" %row
print cur.rowcount
conn.commit()
cur.close()
conn.close()