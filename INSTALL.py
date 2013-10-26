#!/usr/bin/env python2.7
# Filename: INSTALL.sh
# Author:   LIU Yang
# Create Time: Sat Oct 26 13:15:39 HKT 2013
# License:     LGPL v2.0+
# Contact Me:  JeremyRobturtle@gmail.com
'''Simple install script of newycm_extra_conf.py
'''
import argparse
import os
import subprocess
from newycm_extra_conf import DICT_FNAME_IN
import shutil

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--template_path', action='store', dest='tpath',
        default='$HOME/Templates',
        help='Where do you want to install the templates?')

PARSER.add_argument('--bin_path', action='store', dest='bpath',
        default='$HOME/bin',
        help='Where do you want to install the executable?')

def main():
    '''Main process'''
    args = PARSER.parse_args()

    # Parse shell environ variables, e.g., $HOME
    tpath = subprocess.check_output('echo '+args.tpath, shell=True).rstrip()
    bpath = subprocess.check_output('echo '+args.bpath, shell=True).rstrip()

    print("tpath: ".format(args.tpath))

    if not os.path.exists(tpath):
        os.makedirs(tpath)
    if not os.path.exists(bpath):
        os.makedirs(bpath)

    templates = DICT_FNAME_IN.values()
    for template in templates:
        if not os.path.exists(os.path.join(tpath, template)):
            print("INSTALL {:20s} ==> {}".format(template, tpath))
            shutil.copy(template, tpath)
        else:
            print("{} already exists".format(template))
    if not os.path.exists(os.path.join(bpath, 'newycm_extra_conf.py')):
        print("INSTALL {:20s} ==> {}".format('newycm_extra_conf.py', bpath))
        shutil.copy('newycm_extra_conf.py', bpath)
    else:
        print("{} already exists".format('newycm_extra_conf.py'))

if __name__ == '__main__':
    main()
