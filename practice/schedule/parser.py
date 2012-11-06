#!/usr/bin/env python
import re, urllib.request, sys
from html.parser  import HTMLParser
from urllib.error import HTTPError,URLError

"""
Very silly parser for 
http://www.hof-university.de/index.php?id=515&st=Inf&fs=4&jahr=2012&semester=SS

(Hey, it works!)
"""
class TableHTMLParser(HTMLParser):
    def __init__(self):
        super(TableHTMLParser,self).__init__()
        self.interest = False
        self.lastday  = "Montag"
        self.dataset  = []
        self.plandict = {}

    def __add_record(self,data):
        self.plandict[self.lastday] = self.dataset
        self.dataset = []
        self.lastday = data

    def handle_starttag(self, tag, attrs):
        if tag == 'td' and ('class','data') in attrs:
            self.interest = True

    def handle_endtag(self, tag):
        self.interest = False

    def handle_data(self, data):
        if self.interest and data != '\n':
            data = data.strip()
            if data in ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]:
                self.__add_record(data)
            elif data != '':
                self.dataset.append(data)

    def get_table(self):
        self.__add_record(self.lastday)

        struct = {}
        for k,v in self.plandict.items():
            record = []
            part   = []
            for data in v:
                data = re.sub(r'-*','',data).strip()
                part.append(data)
                if re.search('F[A-Z][0-9]*',data):
                    record.append(tuple(part))
                    part = []

            if len(v) != 0:
                struct[k] = record

        return struct

    def print_table(self,table):
        for k,v in table.items():
            print(k)
            for t in v:
                print('{time:18} {room:15} {name:32} {prof}'.format(
                    time =  (t[0] + " bis " + t[1]),
                    room = t[-1],
                    name = t[2],
                    prof = t[-3]))

        
class Download():
    def __init__(self,**param):
        self.url = "http://www.hof-university.de/index.php?id=515&st={st}&fs={fs}&jahr=2012&semester=SS".format(**param)
        try:
            handle = urllib.request.urlopen(self.url)
            self.data = str(handle.read(),'UTF-8')
        except HTTPError as e:
            print("Unable to load URL:",e,self.url)
            sys.exit(-1)
        except URLError as e:
            print("Invalid URL:",e,self.url)
            sys.exit(-2)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('{} <Studiengang> <Fachsemester>'.format(sys.argv[0]))

    urlinfo = {
       'st': sys.argv[1],
       'fs': sys.argv[2]
    }

    d = Download(**urlinfo)
    
    parser = TableHTMLParser()
    parser.feed(d.data)
    parser.print_table(parser.get_table())
