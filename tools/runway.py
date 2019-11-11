#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et
import math

## Runway
#  Manage runway data
#
#  Adrien Crovato
class Runway:
    def __init__(self, xmlRunway):
        self.name = xmlRunway.findtext('NAME')
        self.surface = xmlRunway.findtext('SFC')
        self.length = xmlRunway.findtext('LENGTH')
        self.lengthUnit = xmlRunway.find('LENGTH').get('UNIT')
        self.width = xmlRunway.findtext('WIDTH')
        self.widthUnit = xmlRunway.find('WIDTH').get('UNIT')
        self.length = int(math.ceil(float(self.length)))
        self.width = int(math.ceil(float(self.width)))
        
    def toSQL(self, cursor, id, aId):
        '''Write to SQLite database
        '''
        cursor.execute('INSERT INTO Runways VALUES (?,?,?,?,?,?,?,?)',
            (id,
            aId,
            self.name,
            self.surface,
            self.length,
            self.lengthUnit,
            self.width,
            self.widthUnit))
        
    def write(self):
        '''Print data to console
        '''
        print '--- Runway ---'
        print 'Name:', self.name
        print 'Surface:', self.surface
        print 'Length:', self.length, self.lengthUnit
        print 'Width:', self.width, self.widthUnit
