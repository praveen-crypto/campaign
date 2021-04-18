from campaign import app
from flask import render_template, request, jsonify
from campaign import views
from campaign import mail

#for testing purpose
import json

# ===============================AUTHENTICATION ROUTING 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method=="POST"):
        return True
    elif(request.method=="GET"):
        return render_template('auth/login.html' )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method=="POST"):
        return True
    elif(request.method=="GET"):   
        return render_template('auth/register.html' )


# =================================GENERAL ROUTING
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
        res = views.new_campaign(request)
        return res
    return render_template('common/campaign.html', campaign="active")

@app.route('/about')
def about():
    return render_template('common/about.html', about="active")

@app.route('/contact_us')
def contact_us():
    return render_template('common/contact_us.html', contact_us="active")


# ===========================FOR TESTING PURPOSE
@app.route('/test')
def test():
    if (request.method == "POST"):
       rv = views.new_campaign(request)

       return rv
    else:
        
        rv =  mail.send()
        print(rv)
        return str(rv)


