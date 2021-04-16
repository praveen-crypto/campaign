from campaign import app
from flask_mysqldb import MySQL

mysql = MySQL(app)

def fetchItem():
    cur = mysql.connection.cursor()
    print("cursor:", cur)
    cur.execute(''' SELECT * FROM userdetail ''')
    rv = cur.fetchall()
    return rv