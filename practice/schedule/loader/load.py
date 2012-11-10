#!/usr/bin/env python
# encoding: utf-8

import json
import glob

class NoSuchCourse(Exception):
    pass


def load(studiengang, semester):
    '''
    Lade
    '''
    try:
        path = 'data/%s%d.json' % (studiengang, semester)
        with open(path, 'r') as f:
            return json.load(f)
    except IOError:
        raise NoSuchCourse('Cannot locate ' + path)


def count(studiengang='', semester=-1):
    '''
    Zähle
    '''
    semester_str = '' if semester is -1 else str(semester)
    return len(glob.glob('data/%s%s*.json' % (studiengang, semester_str)))
