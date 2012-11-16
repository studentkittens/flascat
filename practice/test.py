#!/usr/bin/env python
# encoding: utf-8

import urllib
import unittest
import json
import sys

###########################################################################
#                                 Helper                                  #
###########################################################################


def construct_url(*args):
    return '/'.join(['http://localhost:5000/api'] + map(urllib.quote, args))


def download(url):
    print('** Querying: ' + url)
    try:
        return urllib.urlopen(url).read()
    except IOError:
        return ''


def convert(json_data):
    try:
        return json.loads(json_data)
    except ValueError:
        return json_data


def request(*args):
    return convert(download(construct_url(*args)))


###########################################################################
#                               Test Cases                                #
###########################################################################

class TestA(unittest.TestCase):
    def runTest(self):
        print('** Running Tests for a')
        self.test_reachable()
        self.test_get()
        print('** Done!')

    def test_reachable(self):
        data = request()
        self.assertTrue(len(data) > 0, 'API Root not reachable (Server running?)')

    def test_get(self):
        data = request('Inf', '5')
        contain = {
                "room": "Ex_Virtuell",
                "name": "Gender und Diversity",
                "time": "04:00-05:30",
                "prof": "Dozent der VHB",
                "type": "AWM:1",
                "desc": "Virtuelle Vorlesung"
        }
        self.assertTrue(contain in data['Montag'])


class TestB(unittest.TestCase):
    def runTest(self):
        print('** Running Tests for b)')
        self.test_reachable()
        self.test_listcourses()
        self.test_countall()
        self.test_countinf()
        print('** Done!')

    def test_reachable(self):
        data = request()
        self.assertTrue(len(data) > 0, 'API Root not reachable (Server running?)')

    def test_listcourses(self):
        data = request('list_courses')
        self.assertTrue(len(data) == 30)
        self.assertTrue('Inf' in data)
        self.assertTrue('Vinf' in data)
        self.assertTrue('BW' in data)

    def test_countall(self):
        data = request('count', 'all')
        self.assertTrue(int(data) == 84)

    def test_countinf(self):
        data = request('count', 'Inf')
        self.assertTrue(int(data) == 3)

if __name__ == '__main__':
    suite = unittest.TestSuite()

    if 'a' in sys.argv:
        suite.addTest(TestA())

    if 'b' in sys.argv:
        suite.addTest(TestB())

    if 'a' not in sys.argv and 'b' not in sys.argv:
        print('Usage: ' + sys.argv[0] + ' (a|b)')
        sys.exit(-1)

    unittest.TextTestRunner().run(suite)
