import json
import glob


def load(studiengang, semester):
    with open('../data/%s%d.json', 'r') as f:
        data = json.load(f)
    return data


def count(studiengang='', semester=-1):
    semester_str = '' if semester is -1 else str(semester)
    return len(glob.glob('../data/%s%s*.json' % (studiengang, semester_str)))
