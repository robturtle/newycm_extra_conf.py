#!/usr/bin/env python2.7
# Filename: newycm_extra_conf.sh
# Author:   LIU Yang
# Create Time: Fri Oct 25 20:12:15 HKT 2013
# License:     LGPL v2.0+
# Contact Me:  JeremyRobturtle@gmail.com
'''Create a new configure file for YouCompleteMe.

YouCompleteMe is a syntasitcs completion plugin for vim

When invoked, the configure file of that language would
be created under current directory.

For more usage info, call this script with '-h' option.
'''
import argparse
import os
import subprocess
import shutil

_VERSION = '0.2' # 2013-10-27 02:01:31

SRC_PATH = "$NAME/Templates"
_FNAME_OUT = '.ycm_extra_conf.py'
DICT_FNAME_IN = {
        'c++' : 'ycm.cpp.py',
        'c'   : 'ycm.c.py',
        }

LIBS_LIST = ('qt', 'opencv')
DICT_LIBS_FNAME = {
        'qt'     : 'ycm.cpp.qt.py',
        'opencv' : 'ycm.cpp.opencv.py',
        }

PARSER = argparse.ArgumentParser(version=_VERSION)

PARSER.add_argument('--lang', action='store', dest='language',
        default='c++',
        help='Choose language to be supported. Default is c++')

PARSER.add_argument('-l', nargs='*', dest='libs',
        choices=LIBS_LIST,
        help='Add library support')

PARSER.add_argument('--path', action='store', dest='path',
        default='$HOME/Templates',
        help='''Specify path to .ycm_extra_conf.py templates.
        Default is "$HOME/Templates/"''')


def main():
    '''Main process.'''
    args = PARSER.parse_args()

    fname_in = DICT_FNAME_IN[args.language]
    # Parse shell environment variables:
    path = subprocess.check_output('echo '+args.path, shell=True).rstrip()
    fname_in = os.path.join(path, fname_in)
    if not os.path.exists(fname_in):
        raise OSError(fname_in)

    shutil.copy(fname_in, _FNAME_OUT)

    if args.libs:
        with open(_FNAME_OUT, 'a') as outf:
            for lib in args.libs:
                libf_path = os.path.join(path, DICT_LIBS_FNAME[lib])
                with open(libf_path) as libf:
                    lib_config = libf.read()
                    outf.write(lib_config)

if __name__ == '__main__':
    try:
        main()
    except OSError, fname:
        print("Template file {} not exists!\n"
              "Use --path=PATH option to specify "
              "template directory".format(fname))
