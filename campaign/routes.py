from campaign import app
from flask import render_template, request, jsonify,  redirect, url_for, session
from campaign import views
from campaign import mail

#for testing purpose
import json

app.secret_key = b't4\xbb\x96\xdf\x1d\x7fni\xa1dT\xe0h\x0e\x8a'


# ===============================AUTHENTICATION ROUTING 
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if (request.method=="POST"):
        res = views.signin(request)
        if res:
            userid = session['id']
            return render_template('common/monitor.html', monitor="active", userid = userid)
        return res
    elif(request.method=="GET"):
        if session['id'] == '':
            print("session id1:",session['id'])
            return render_template('auth/sign_in.html' )
        else:
            print("session id2:",session['id'])
            return render_template('common/monitor.html', monitor="active")


@app.route('/signup', methods=['GET', 'POST'])
def register():
    if (request.method=="POST"):
        return True
    elif(request.method=="GET"):   
        return render_template('auth/sign_up.html' )






# =================================GENERAL ROUTING
@app.route('/')
@app.route('/home')
def home():
    
    return render_template('common/landing_page.html', home="active")


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


