from flask import render_template, request, jsonify, redirect, url_for, session
from campaign import database
import json
import math, random
from campaign import mail

# function to generate OTP
def generateOTP() :
    # Declare a digits variable  
    # which stores all digits 
    digits = "0123456789"
    OTP = ""
   # length of password can be chaged
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    
    return str(OTP)


def new_campaign(request):
    try:
        if request.method != "POST":
            return "BAD REQUEST"
        dat = []
        da = request.form.get('data')
        da = json.loads(da)
        for i in da.values():
            dat.append(i)
        
        data = tuple(dat)
        if(database.new_campaign(data)):
            
            return jsonify(message='OK',status=200)
        else:
            message,status = "FAILED", 200
            return jsonify(message, status)
    except Exception as e:
        print(e)
        message, status = "SERVER ERROR", 500
        return jsonify(message, status)


def signin(request):
    try:
        if request.method != "POST":
            return "BAD REQUEST"

        dat = []
        da = request.form.get('data')
        da = json.loads(da)
        for i in da.values():
            dat.append(i)
        data = tuple(dat)

        account = list(database.signin(data))
        print('account:', account)
        if account:
            session['loggedin'] = True
            session['id'] = account[13]
            session['username'] = account[0]
            return True
        else:
            message,status = "FAILED", 200
            return jsonify(message, status)
    except Exception as e:
        print(e)
        message, status = "SERVER ERROR", 500
        return jsonify(message, status)


def verify_email(request):
    try:
        if request.method != "POST":
            return "BAD REQUEST"

        dat = []
        da = request.form.get('data')
        da = json.loads(da)
        for i in da.values():
            dat.append(i)

        dat.append(generateOTP())
        print("data",dat)
        if mail.send(dat[1], dat[3]):
            data = tuple(dat)
            res, otpid =  database.verify_otp(data) 
        
        if res:
            message,status = "SUCCESS", 200
            return jsonify(message, status, otpid)
        else:
            message,status = "FAILED", 200
            return jsonify(message, status)
    except Exception as e:
        print(e)
        message, status = "SERVER ERROR", 500
        return jsonify(message, status)

def get_current_campaign():
    link = database.get_current_campaign()
    return link