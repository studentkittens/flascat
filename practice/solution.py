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
    return '<b>Musterlösung.</b>'


###########################################################################
#                               Aufgabe a)                                #
###########################################################################

@app.route('/api/<studiengang>/<semester>')
def api_root(studiengang, semester):
    try:
        return json.dumps(load(studiengang, semester))
    except NoSuchCourse:
        return '{}'


###########################################################################
#                               Aufgabe b)                                #
###########################################################################


@app.route('/api/list_courses')
def api_list_courses():
    return str(sorted(list_courses()))


###########################################################################
#                               Aufgabe c)                                #
###########################################################################


@app.route('/api/count/<studiengang>')
def api_count(studiengang):
    if studiengang == 'all':
        return str(count())
    else:
        return str(count(studiengang))


###########################################################################
#                               Aufgabe d)                                #
###########################################################################


@app.route('/view/<studiengang>/<semester>')
def view(studiengang, semester):
    try:
        loaded = load(studiengang, semester)
        return render_template('table.html', input_data=loaded)
    except NoSuchCourse:
        return render_template('table.html', input_data={})

###########################################################################
#                              Let it run...                              #
###########################################################################

if __name__ == '__main__':
    app.run(debug=True)