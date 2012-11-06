#!/usr/bin/env python
# encoding: utf-8

import parser as p
import os

def parse(sem, stg):
    parser = p.TableHTMLParser()
    parser.feed(p.download_schedule(
       studiengang=stg,
       semester=sem))
    parser.print_table()

    with open(os.path.join('data', stg + sem + '.json'), 'w') as f:
        f.write(parser.get_json())


if __name__ == '__main__':
    with open('ws2012.list', 'r') as f:
        for line in f:
            result = line.split()
            stname = result[-1].replace('_',' ')
            sem = result[:-2]
            print(stname, '=', end=' ')
            for x in sem:
                print(type(x), x, end=' ')
                try:
                    parse(str(x), str(stname))
                except IndexError:
                    pass
            print()

