#test
import pymysql
conn = pymysql.connect(host='127.0.0.1',#unix_socket='/tmp/mysql.sock',
        user='root',passwd='843800695',db='oracle',charset='utf8')
cur = conn.cursor()
cur.execute("select * from news")

# print(cur.fetchone())
cur.close()
conn.close()