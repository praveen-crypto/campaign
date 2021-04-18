from flask import render_template, request, jsonify, redirect, url_for, session
from campaign import database
import json


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



