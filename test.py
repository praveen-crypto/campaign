from flask import Flask, render_template, url_for

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = ""
app.config['MYSQL_PORT'] = ""
app.config['MYSQL_USER'] = "praveen"
app.config['MYSQL_PASSWORD'] = "1234"
app.config['MYSQL_DB'] = "campaign"
app.config['MYSQL_CHARSET'] = ""

mysql = MySQL(app)

@app.route("/")
def fetchItem():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM userdetail''')
    rv = cur.fetchall()
    return str(rv[0])

if __name__ == "__main__":
    app.run(debug=True)