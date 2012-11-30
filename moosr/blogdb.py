#!/usr/bin/env python
# encoding: utf-8


"""
How to share g, db to exclude db module?
"""
import sqlite3
from contextlib import closing
from moosr import app
from flask import flash, g


def get_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return entries


def add_entry():

    g.db.execute('insert into entries (title, text) values (?, ?)',
                 ["das hier ist ein titel", "das hier ist ein wunderschoner text"])
    g.db.commit()
    flash('New entry was successfully posted')


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('database.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


def connect_db():
    return sqlite3.connect('moosr.db')


def setup():
    g.db = connect_db()


def teardown(exception):
    g.db.close()
