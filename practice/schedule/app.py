#!/usr/bin/env python
# encoding: utf-8

'''
Das ist die eigentliche Anwendung die ihr schreiben sollt.

Da wir nette Leute sind haben wir euch ein Skelett bereitgestellt.
'''

import json
from flask import Flask
from loader.load import load, count, NoSuchCourse

app = Flask('practice')


@app.route('/')
def root():
    return '<b>Well nothing here yet</b>'


@app.route('/api/<studiengang>/<int:semester>')
def api(studiengang, semester):
    try:
        return json.dumps(load(studiengang, semester))
    except NoSuchCourse:
        return '"no results"', 404


@app.route('/api/count')
def api_count():
    return str(count())


@app.route('/api/search')
def api_search():
    return '...'

if __name__ == '__main__':
    app.run(debug=True)
