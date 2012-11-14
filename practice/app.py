#!/usr/bin/env python
# encoding: utf-8

'''
Das ist die eigentliche Anwendung die ihr schreiben sollt.
Unten findet ihr bereits eine minimale Flask Anwendung.

Jetzt müsst ihr sie nur noch erweitern.
'''

# Imports sind von der Musterlösung. Kleiner Hint...
import json
from flask import Flask, render_template, redirect
from loader.load import load, count, list_courses, NoSuchCourse

app = Flask('practice')


@app.route('/')
def root():
    return '<b>Well nothing here yet. Thats your job.</b>'


@app.route('/api')
def api_root():
    return load('Inf', '5')

###########################################################################
#                              Let it run...                              #
###########################################################################

if __name__ == '__main__':
    app.run(debug=True)
