from campaign import app
from campaign.db_config import host,password,port,user,database
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json

# DATABASE CONFIGURATION
app.config['MYSQL_HOST'] = host
app.config['MYSQL_PORT'] = port
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = database
app.config['MYSQL_CHARSET'] = "utf8mb4"

mysql = MySQL(app)

def fetchItem():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(''' SELECT * FROM userdetail ''')
    rv = cursor.fetchall()
    return rv

def new_campaign(data):
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        columns = "username,phone,email,company_name,brand,promote,objective,start_date,end_date,total_days,procontent,total_cost,link,content_type"
        values = ''
        for i in range(len(data)):
            
            values += " '"+str(data[i])+"',"
            #print(values)
            #print("data type",type(data[i]))
        values = values[:-1]
        print(values)
        status = cursor.execute("INSERT INTO userdetail (username,phone,email,company_name,brand,promote,objective,start_date,end_date,total_days,procontent,total_cost,link,content_type) VALUES ({})".format(values))
        #
        mysql.connection.commit()
        print(status)
        return True        
    except Exception as e:
        print(e)
        return False
    
