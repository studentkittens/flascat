#!/usr/bin/env python
# encoding: utf-8

import urllib
import unittest
import json


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

class TestRestInterface(unittest.TestCase):

    def test_reachable(self):
        data = request()
        self.assertTrue(len(data) > 0, 'API Root not reachable (Server running?)')

    def test_listcourses(self):
        data = request('list')
        self.assertTrue(len(data) > 10)
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
    unittest.main()

