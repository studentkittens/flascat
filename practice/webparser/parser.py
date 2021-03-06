#!/usr/bin/env python
# encoding: utf-8

import re, sys, urllib, json
from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import quote

headers = ['room', 'type', 'time', 'note', 'prof', 'name', 'desc']


def looks_like_room(data):
    return re.match('F[A-Z][0-9]{3}', data) or re.match('Ex_*', data)


def looks_like_day(data):
    data = data.lower().strip()
    result = data in  ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    return result or data in ["montag", "dienstag", "mittwoch", "donnerstag", "freitag"]


def looks_like_prof(data):
    tags = ['Herr', 'Prof.', 'Dr.']
    for tag in tags:
        if tag in data:
            return True
    else:
        # Check if it consists of two words (Firstname Lastname)
        # (This should be easier with \w but I'm to dumb right now)
        return re.match('[A-Z][a-z]+\s+[A-Z][a-z]+', data)


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
        self._node_idx = 0
        self._schedule_started = False

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
            if looks_like_day(data):
                # Add a day as key to the dictionary:
                self._current_list = self.schedule.setdefault(data, [{}])
                self._schedule_started = True
            elif data and self._schedule_started:
                node = self._current_list[-1]
                key = guess_key_from_data(data)

                if node.get(key):
                    node[key] += ('#' + data)
                else:
                    node[key] = data

                # Match a room like FD177, if so we open a new Node
                if looks_like_room(data):
                    self._current_list.append({})

    def feed(self, input_data):
        HTMLParser.feed(self, input_data)
        self.sanitize_dict()

    def sanitize_dict(self):
        for day, data in self.schedule.items():
            for idx, node in enumerate(data):
                if len(node) < 2:
                    del self.schedule[day][idx]
                else:
                    # Sanitize time:
                    if node.get('time'):
                        node['time'] = node['time'].replace('#', '-')

                    # Process _tmp
                    if node.get('_tmp'):
                        split = node.get('_tmp').split('#')
                        node['name'] = split[0]
                        del split[0]

                        # Find something that looks like Prof
                        for data in split:
                            if looks_like_prof(data):
                                node['prof'] = data
                                split.remove(data)

                        if len(split) > 2:
                            node['desc'] = '\n'.join(split)
                        del node['_tmp']

    def print_table(self):
        print(json.dumps(self.schedule, indent=4))

    def get_json(self):
        return json.dumps(self.schedule, indent=4)


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
