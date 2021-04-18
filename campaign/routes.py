from campaign import app
from flask import render_template, request, jsonify
from campaign import views

#for testing purpose
from campaign.database import fetchItem, new_campaign
import json


@app.route('/')
@app.route('/home')
def home():
    
    return render_template('common/landing_page.html', home="active" )

@app.route('/monitor')
def monitor():
    return render_template('common/monitor.html', monitor="active")

@app.route('/new_campaign', methods=['GET', 'POST'])
@app.route('/campaign')
def campaign():
    if request.method == 'POST':
        views.new_campaign(request)
    return render_template('common/campaign.html', campaign="active")

@app.route('/about')
def about():
    return render_template('common/about.html', about="active")

@app.route('/contact_us')
def contact_us():
    return render_template('common/contact_us.html', contact_us="active")


@app.route('/test')
def test():
    if (request.method == "POST"):
       data = []
       for item in json.loads(request.form.get('data')).values():
           data.append(item)
       rv = new_campaign(data)        
    rv =  str(fetchItem())
    return rv


