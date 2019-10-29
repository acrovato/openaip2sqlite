#!/usr/bin/env python
# -*- coding: utf8 -*-

## Country
#  Manage country data
#
#  Adrien Crovato
class Country:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        
    def toSQL(self, fsql):
        '''Write to SQLite database
        '''
        print 'oops'
        
    def write(self):
        '''Print data to console
        '''
        print '--- Country ---'
        print 'Name:', self.name
        print 'Code:', self.code
