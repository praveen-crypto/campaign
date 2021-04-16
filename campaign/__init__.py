from flask import Flask, render_template, url_for

app = Flask(__name__)

# DATABASE CONFIGURATION
app.config['MYSQL_HOST'] = ""
app.config['MYSQL_PORT'] = ""
app.config['MYSQL_USER'] = "praveen"
app.config['MYSQL_PASSWORD'] = "1234"
app.config['MYSQL_DB'] = "campaign"
app.config['MYSQL_CHARSET'] = ""

from campaign import routes

 
