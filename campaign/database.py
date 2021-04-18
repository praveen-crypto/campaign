from campaign import app
from campaign.db_config import HOST,PASSWORD,PORT,USER,DATABASE
import mysql.connector
import json

def connector():
    try:
        mydb = mysql.connector.connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DATABASE,
                port = PORT
                )
        return mydb
    except Exception as e:
        print(e)
        return None


def fetchItem():
    try:
        connection  = connector()
        cursor = connection.cursor()
        cursor.execute(''' SELECT * FROM userdetail ''')
        rv = cursor.fetchall()
        
        return rv
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()


def new_campaign(data):
    try:
        connection  = connector()
        cursor = connection.cursor()
        columns = "username,phone,email,company_name,brand,promote,objective,start_date,end_date,total_days,procontent,total_cost,link,content_type"
        values=data
        #print("values:",values)
        sql = "insert into userdetail({}) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(columns)
        cursor.execute(sql,values)
        connection.commit()

        return True
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()


def signin(data):
    try:
        connection  = connector()
        cursor = connection.cursor()
        columns = "email,password"
        values=data
        print("Entered Credentials:",values)
        #'SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password)
        sql = "SELECT * FROM userdetail WHERE email = %s AND password = %s"
        cursor.execute(sql,values)
        res = cursor.fetchone()
        connection.commit()
        return res
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()



def register(data):
    try:
        connection  = connector()
        cursor = connection.cursor()
        columns = "username,email,password,otp"
        values = data
        sql = "insert into userdetail({}) values(%s,%s,%s,%s)".format(columns)
        cursor.execute(sql,values)
        connection.commit()

        return True
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()



