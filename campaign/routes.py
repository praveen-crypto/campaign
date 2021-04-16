from campaign import app
from flask import render_template
from campaign.database import fetchItem

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