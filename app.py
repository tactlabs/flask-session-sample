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
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

app = Flask(__name__)

app.secret_key = "LaEt{B07|MCCtC0.(OGw0B[-AUTs"

SESSION_KEY = "user_session"

def requires_session(f):
  
    @wraps(f)
    def decorated(*args, **kwargs):

        # print('inside deco')
    
        # check apikey in args
        if SESSION_KEY not in session:

            # print('session not available')

            data = {
                'apiresult' : 'Session Not Available',
                'apimessage': 1011
            }

            return jsonify(data)

        # print('session is available')

        # verify user_session
        user_session = session.get(SESSION_KEY)

        return f(*args, **kwargs)

    return decorated

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
@requires_session # Decorator has to be close to the method
def user_content():
    return 'User Content'

'''
    http://localhost:5000/login

    http://localhost:5000/login?email=raja@gmail.com&password=abcd
    http://localhost:5000/login?email=one&password=two
'''
@app.route('/login')
def login():

    email = request.values.get('email')
    password = request.values.get('password')

    if(email == 'raja@gmail.com' and password == 'abcd'):

        # set session
        session[SESSION_KEY] = 'session_key_raja'

        return "Success"

    return 'Login Failed'

'''
    http://localhost:5000/get/session
'''
@app.route('/get/session')
def get_session():

    return session[SESSION_KEY]

'''
    http://localhost:5000/logout
'''
@app.route('/logout')
def logout():

    del session[SESSION_KEY]

    return "Logged out"


if __name__ == '__main__':
    app.run(debug=True)