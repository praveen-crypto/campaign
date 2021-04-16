from flask import Flask, render_template, url_for
from campaign.db_config import host,password,port,user,database
app = Flask(__name__)

# DATABASE CONFIGURATION
app.config['MYSQL_HOST'] = host
app.config['MYSQL_PORT'] = port
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = database
app.config['MYSQL_CHARSET'] = ""

from campaign import routes

 
