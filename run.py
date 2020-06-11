#!/usr/bin/env python
# -*- coding: utf8 -*-
# test encoding: à-é-è-ô-ï-€
#
## @package openaip2sqlite
#  Convert openAIP XML files to SQLite database
#
#  Adrien Crovato

def setup(xmldir):
    '''Perform basic setup
    '''
    import sys, os
    sys.path.append(os.path.dirname(os.path.realpath(__file__))) # adds "." to the python path
    # create output directory
    idir = os.path.join(os.getcwd(), xmldir)
    odir = os.path.join(os.getcwd(), 'sqlite')
    if not os.path.isdir(odir):
        print "creating", odir
        os.makedirs(odir)
    os.chdir(odir)
    return idir
    
def printStart():
    import time, socket
    print '*' * 79
    print '* openaip2sqlite'
    print '* Adrien Crovato, June 2020'
    print '* Distributed under Apache license 2.0'
    print '*' * 79
    print 'time:', time.strftime('%c')
    print 'hostname:', socket.gethostname()
    print '*' * 79
    
def printEnd():
    print '*' * 79
    print 'Job done!'
    print '*' * 79

def main(verbose, xmldir, airac):
    import tools.manager as man
    # start
    xmlpath = setup(xmldir)
    printStart()
    # run
    manager = man.Manager(airac, xmlpath, verbose)
    manager.run() 
    # end
    printEnd()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', help='print parsed data to console',  action="store_true")
    parser.add_argument('dir', help='xml source directory')
    parser.add_argument('a', help='AIRAC number')
    args = parser.parse_args()
    main(args.verbose, args.dir, args.a)