#!/usr/bin/env python
# encoding: utf-8

'''
Das ist die eigentliche Anwendung die ihr schreiben sollt.
Unten findet ihr bereits eine minimale Flask Anwendung.

Jetzt müsst ihr sie nur noch erweitern.
'''

# Imports sind von der Musterlösung. Kleiner Hint...
import json
from flask import Flask, render_template
from loader.load import load, count, list_courses, NoSuchCourse

###########################################################################
#                           Was schon da ist...                           #
###########################################################################

app = Flask('practice')


@app.route('/')
def root():
    return '<b>Your job to fill something in here.</b>'

###########################################################################
#                              Let it run...                              #
###########################################################################

if __name__ == '__main__':
    app.run(debug=True)
