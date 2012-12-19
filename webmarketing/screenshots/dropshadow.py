#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import glob
import subprocess

PREFIX = 'old_'

cmd = "convert {0} \( +clone  -background black  -shadow 80x3+5+5 \) +swap -background none -layers merge +repage {1}"
srcdir = sys.argv[1]
content = glob.glob1(srcdir, '*.png')
for item in content:
    curfile = os.path.join(srcdir, item)
    oldfile = os.path.join(srcdir, PREFIX + item)
    os.rename(curfile, oldfile)
    subprocess.call(cmd.format(oldfile, curfile), shell=True)
