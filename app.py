from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# DATABASE CONFIGURATION

app.config['MYSQL_HOST'] = ""
app.config['MYSQL_PORT'] = ""
app.config['MYSQL_USER'] = ""
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = ""
app.config['MYSQL_CHARSET'] = ""

mysql = MySQL(app)

def fetchItem():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM userdetail''')
    rv = cur.fetchall()
    return rv


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/home')
def home():
    items = fetchItem()
    return render_template('home.html', home="active", item = items)

@app.route('/monitor')
def monitor():
    return render_template('monitor.html', monitor="active")

@app.route('/campaign')
def campaign():
    return render_template('campaign.html', campaign="active")

@app.route('/about')
def about():
    return render_template('about.html', about="active")

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html', contact_us="active")





if __name__ == "__main__":
    app.run(debug=True)
