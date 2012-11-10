#!/usr/bin/env python
# encoding: utf-8

import json
import glob


class NoSuchCourse(Exception):
    pass


def load(studiengang, semester):
    try:
        path = 'data/%s_%d.json' % (studiengang, semester)
        with open(path, 'r') as f:
            return json.load(f)
    except IOError:
        raise NoSuchCourse('Cannot locate ' + path)


def count(studiengang='', semester=-1):
    if studiengang:
        return len(glob.glob('data/%s_*.json' % studiengang))
    else:
        return len(glob.glob('data/*.json'))

def list_courses():
    jsons = glob.glob('data/*.json')
    return list(set([path.split('_')[0][len('data/'):] for path in jsons]))
