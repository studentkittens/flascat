#!/usr/bin/env python
# encoding: utf-8

from __future__ import with_statement
import sqlite3
from moosr import app
from contextlib import closing
from flask import Flask, request, g, redirect, url_for

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
# all the imports

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])



