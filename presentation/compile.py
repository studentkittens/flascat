#!/usr/bin/env python
# encoding: utf-8

# Run with Python3
import os, sys, shutil, subprocess, time


def copy_each_from(src, dest):
    '''
    Boils down to: cp src/* dest/

    :src: Source Path (A directory)
    :dest: Destination Path (A directory)
    '''
    relfiles = (os.path.join(src, f) for f in os.listdir(src))
    for path in filter(os.path.isfile, relfiles):
        shutil.copy(path, dest)


def compile():
    '''
    Make the impress-magic happen
    '''
    shutil.rmtree('static', ignore_errors=True)
    shutil.copytree('_static', 'static')
    copy_each_from('_static', 'html/static')
    shutil.rmtree('html/_images', ignore_errors=True)
    shutil.copytree('_static', 'html/_images')
    subprocess.call(['impress'])


def usage():
    'Print the usage'
    print('%s (--loop|--help)', sys.argv[0])
    sys.exit(-1)


if __name__ == '__main__':
    if '--help' in sys.argv:
        usage()

    if '--loop' in sys.argv:
        try:
            while True:
                compile()
                print('Done.')
                time.sleep(1)
        except KeyboardInterrupt:
            print('Interrupted.')
    else:
        compile()
