#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, redirect
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Elk!"


@app.route("/elkpowerz")
def power_elk():
    return redirect('http://www.google.de')


if __name__ == "__main__":
        app.run(debug=True)
