#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et

## Frequency
#  Manage frequency data
#
#  Adrien Crovato
class Frequency:
    def __init__(self, xmlFrequency):
        self.callsign = xmlFrequency.findtext('DESCRIPTION')
        self.frequency = xmlFrequency.findtext('FREQUENCY')
        self.category = xmlFrequency.get('CATEGORY')
        self.type = xmlFrequency.findtext('TYPE')
        

    def toSQL(self, fsql):
        '''Write to SQLite database
        '''
        print 'oops'
        
    def write(self):
        '''Print data to console
        '''
        print '--- Frequency ---'
        print 'Callsign:', self.callsign
        print 'Frequency:', self.frequency
        print 'Category:', self.category
        print 'Type:', self.type
