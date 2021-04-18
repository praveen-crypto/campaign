from flask import render_template, request, jsonify
from campaign import database
import json


def new_campaign(request):
    try:
        if request.method != "POST":
            return "BAD REQUEST"
        data = []
        for item in json.loads(request.form.get('data')).values():
            data.append(item)
        #print("DATA TYPE:", data )
        #data = json.loads(request.form.get('data'))
        if(database.new_campaign(data)):
            message,status = "OK", 200
            return message, status
        else:
            message,status = "FAILED", 200
            return message, status
    except Exception as e:
        print(e)
        message, status = "SERVER ERROR", 500
        return message, status
