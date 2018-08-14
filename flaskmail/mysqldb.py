import MySQLdb

def connection():
    conn=MySQLdb.connect(user="root",passwd="mom0511",db="")
    c=conn.cursor()
    return c,conn
