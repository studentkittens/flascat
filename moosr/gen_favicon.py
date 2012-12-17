#!/usr/bin/env python
# encoding: utf-8

import subprocess
import sys


def create_sizes(input_img):
    for size in [16, 32, 64, 128, 256]:
        subprocess.call('convert {path} -resize {s}x{s} favicon-{s}.png'.format(
            s=size,
            path=input_img
        ), shell=True)

    subprocess.call('convert favicon-16.png favicon-32.png favicon-64.png favicon-128.png favicon-256.png -colors 256 favicon.ico', shell=True)
    subprocess.call('rm favicon-*.png', shell=True)

if __name__ == '__main__':
    create_sizes(sys.argv[1])
