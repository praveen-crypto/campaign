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
            message,status = "OK", 200
            return jsonify(message, status)
        else:
            message,status = "FAILED", 200
            return jsonify(message, status)
        
    elif(request.method=="GET"):
        if 'loggedin' in session:
            return redirect(url_for('home'))
        else:
            return render_template('auth/sign_in.html' )

            

@app.route('/signout', methods=['GET'])
def signout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    print('session:',session)
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if (request.method=="POST"):
        res = views.signup(request)
        return res
    elif(request.method=="GET"):
        if 'loggedin' in session:
            return redirect(url_for('home'))
        else: 
            return render_template('auth/sign_up.html' )



# =================================GENERAL ROUTING
@app.route('/')
@app.route('/home')
def home():
    link = views.get_current_campaign()
    print(link)
    return render_template('common/landing_page.html', home="active", links = link)

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

# ===========================FOR TESTING PURPOSE
@app.route('/test')
def test():
    if (request.method == "POST"):
       rv = views.new_campaign(request)

       return rv
    else:
        return render_template('common/landing_page.html', home="active")
        #rv =  mail.send()
        #print(rv)
        


