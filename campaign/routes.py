from campaign import app
from flask import render_template
from campaign.database import fetchItem


@app.route('/')
@app.route('/home')
def home():
    items = fetchItem()
    return render_template('common/landing_page.html', home="active", item = items)

@app.route('/monitor')
def monitor():
    return render_template('common/monitor.html', monitor="active")

@app.route('/campaign')
def campaign():
    return render_template('common/campaign.html', campaign="active")

@app.route('/about')
def about():
    return render_template('common/about.html', about="active")

@app.route('/contact_us')
def contact_us():
    return render_template('common/contact_us.html', contact_us="active")


