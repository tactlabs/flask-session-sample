#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    
'''

# Import necessary modules
from flask import Flask
import json
from flask import jsonify

app = Flask(__name__)

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