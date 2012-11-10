#!/usr/bin/env python
# encoding: utf-8

'''
Das ist die eigentliche Anwendung die ihr schreiben sollt.

Da wir nette Leute sind haben wir euch ein Skelett bereitgestellt.
'''

import json
from flask import Flask, render_template, redirect
from loader.load import load, count, list_courses, NoSuchCourse

app = Flask('practice')


@app.route('/')
def root():
    return '<b>Well nothing here yet. Thats your job.</b>'

###########################################################################
#                               Aufgabe a)                                #
###########################################################################


@app.route('/api/<studiengang>/<int:semester>')
def api(studiengang, semester):
    try:
        return json.dumps(load(studiengang, semester))
    except NoSuchCourse:
        return redirect('404.html'), 404

###########################################################################
#                               Aufgabe b)                                #
###########################################################################


@app.route('/api/count/<studiengang>')
def api_count_filter(studiengang):
    if studiengang == 'all':
        return str(count())
    else:
        return str(count(studiengang=studiengang))


@app.route('/api/list_courses')
def api_list():
    courses = list_courses()
    courses.sort()
    return json.dumps(courses)


###########################################################################
#                               Aufgabe c)                                #
###########################################################################


@app.route('/view/<studiengang>/<int:semester>')
def view(studiengang, semester):
    try:
        data = load(studiengang, semester)
        data = iter(sorted(data.items()))
        return render_template('hello.html', schedule=data)
    except NoSuchCourse:
        return render_template('hello.html', schedule={})

###########################################################################
#                              Let it run...                              #
###########################################################################

if __name__ == '__main__':
    app.run(debug=True)
