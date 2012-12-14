#!/usr/bin/env python
# encoding: utf-8

import sqlite3
from flask import g


DB_NAME = 'posts_database.db'


def setup():
    g.db = sqlite3.connect(DB_NAME)


def teardown(exception):
    g.db.close()
