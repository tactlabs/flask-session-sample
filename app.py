#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:

    https://overiq.com/flask-101/sessions-in-flask/

    https://stackoverflow.com/questions/26080872/secret-key-not-set-in-flask-session-using-the-flask-session-extension

    https://randomkeygen.com/
    
    https://pythonhosted.org/Flask-Session/ - this is buggy and deprecated
'''

# Import necessary modules
from flask import Flask
import json
from flask import jsonify

from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

app = Flask(__name__)

app.secret_key = "LaEt{B07|MCCtC0.(OGw0B[-AUTs"

'''
    http://127.0.0.1:5000/add-visit/
'''
@app.route('/add-visit/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return "Total visits: {}".format(session.get('visits'))

'''
    http://127.0.0.1:5000/delete-visit/
'''
@app.route('/delete-visit/')
def delete_visits():
    session.pop('visits', None) # delete visits
    return 'Visits deleted'

'''
    http://127.0.0.1:5000/visits-counter/
'''
@app.route('/visits-counter/')
def count():
    if 'visits' in session:
        session['visits'] = session.get('visits')  # reading and updating session data
    else:
        session['visits'] = 0 # setting session data
    return "Total visits: {}".format(session.get('visits'))


'''
    http://localhost:5000/
'''
@app.route('/')
def entry_point():
    return 'Hello World!'

'''
    http://localhost:5000/content
'''
@app.route('/content')
def user_content():
    return 'User Content'


if __name__ == '__main__':
    app.run(debug=True)