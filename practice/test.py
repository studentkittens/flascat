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
        self.test_badinput()
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
                "prof": "Virtuelle Vorlesung",
                "type": "AWM:1"
        }
        self.assertTrue(contain in data['Montag'])

    def test_badinput(self):
        data = request('Inf', '42')
        self.assertTrue({} == data)


class TestB(unittest.TestCase):
    def runTest(self):
        print('** Running Tests for b)')
        self.test_reachable()
        self.test_listcourses()
        print('** Done!')

    def test_reachable(self):
        data = request()
        self.assertTrue(len(data) > 0, 'API Root not reachable (Server running?)')

    def test_listcourses(self):
        data = request('list_courses')
        self.assertTrue(len(data) == 271)
        self.assertTrue('Inf' in data)
        self.assertTrue('Vinf' in data)
        self.assertTrue('BW' in data)


class TestC(unittest.TestCase):
    def runTest(self):
        print('** Running Tests for c)')
        self.test_reachable()
        self.test_countall()
        self.test_countinf()
        print('** Done!')

    def test_reachable(self):
        data = request()
        self.assertTrue(len(data) > 0, 'API Root not reachable (Server running?)')

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

    if 'c' in sys.argv:
        suite.addTest(TestC())

    if suite.countTestCases() is 0:
        print('Usage: ' + sys.argv[0] + ' (a|b|c)')
        sys.exit(-1)

    unittest.TextTestRunner().run(suite)
