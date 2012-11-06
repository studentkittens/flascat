#!/usr/bin/env python
# encoding: utf-8

import re, sys, urllib
from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import quote

from pprint import pprint

'''

# Inf3

11:30
13:00
Formale Sprachen -- -
 - (Inf3 + WI3)
Prof. Dr. Richard Göbel
HF:1
FA009


# Inf5

11:30
13:00
Geographische Informationssysteme -- -
 - (Vinf+Inf+MI 5)
Prof. Dr. Richard Göbel,  Carsten Kropf
FWM:1
FB001/002


'''

headers = ['room', 'type', 'time', 'note', 'prof', 'name', 'desc']


def looks_like_room(data):
    return re.match('F[A-Z][0-9]+', data) or re.match('Ex_*', data)


def guess_key_from_data(data):
    data = data.strip()
    if looks_like_room(data):
        return 'room'
    elif re.match('[A-Z]+:[0-9]', data):
        return 'type'
    elif re.match('[0-9][0-9]:[0-9][0-9]', data):
        return 'time'
    elif re.search('\(.+\)*.', data) and len(data) < 20:
        return 'note'
    else:
        # Not yet defined. Done while sanitizing.
        return '_tmp'


class TableHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__interest = False
        self.schedule = {}
        self._current_list = []
        self._current_idx = 0
        self._node_idx = 0

    def handle_starttag(self, tag, attrs):
        # Be only interested in this <td> tags,
        # that have class= and data= attributes.
        if tag == 'td' and ('class', 'data') in attrs:
            self.__interest = True

    def handle_endtag(self, tag):
        # Always be uninterested by default.
        self.__interest = False

    def handle_data(self, data):
        data = data.strip()
        if self.__interest and len(data) > 0:
            data = re.sub(r'-*', '', data).strip()
            if data in ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]:
                # Add a day as key to the dictionary:
                self._current_list = self.schedule.setdefault(data, [{}])
                self._current_idx = 0
            elif data:
                node = self._current_list[self._current_idx]
                key = guess_key_from_data(data)

                if node.get(key):
                    node[key] += '#' + data
                else:
                    node[key] = data

                # Match a room like FD177, if so we open a new Node
                if looks_like_room(data):
                    self._current_idx += 1
                    self._current_list.append({})

    def feed(self, input_data):
        HTMLParser.feed(self, input_data)
        self.sanitize_dict()

    def sanitize_dict(self):
        for day, data in self.schedule.items():
            for idx, node in enumerate(data):
                if len(node) < 2:
                    del self.schedule[day][idx]
                    continue

                # Sanitize time:
                if node.get('time'):
                    node['time'] = node['time'].replace('#', '-')

                # Process _tmp
                if node.get('_tmp'):
                    split = node.get('_tmp').split('#')
                    node['name'] = split[0]
                    if len(split) > 1:
                        node['prof'] = split[-1]
                    if len(split) > 2:
                        node['desc'] = split[1]
                    del node['_tmp']

    def print_table(self):
        import json
        print(json.dumps(self.schedule, indent=4))


def download_schedule(studiengang, semester):
    data = ''
    url = "http://www.hof-university.de/index.php?id=515&st={st}&fs={fs}&jahr=2012&semester={ws}".format(
            st=quote(studiengang),
            fs=quote(semester),
            ws='WS')
    try:
        print('# Used URL: ', url)
        data = str(urlopen(url).read(), 'UTF-8')
    except urllib.error.HTTPError as e:
        print("Unable to load URL:", e, url)
    except urllib.error.URLError as e:
        print("Invalid URL:", e, url)
    finally:
        return data


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('{} <Studiengang> <Fachsemester>'.format(sys.argv[0]))
        sys.exit(-3)

    parser = TableHTMLParser()
    parser.feed(download_schedule(
       studiengang=sys.argv[1],
       semester=sys.argv[2]))

    parser.print_table()
