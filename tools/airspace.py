#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et

## Airspace
#  Manage airspace data
#
#  Adrien Crovato
class Airspace:
    def __init__(self, xmlAirspace):
        self.country = xmlAirspace.findtext('COUNTRY')
        self.category = xmlAirspace.get('CATEGORY')
        self.name = xmlAirspace.findtext('NAME') # TODO: parse frequency out
        self.ceiling = xmlAirspace.find('ALTLIMIT_TOP').findtext('ALT')
        self.ceilingUnit = xmlAirspace.find('ALTLIMIT_TOP').find('ALT').get('UNIT')
        if self.ceilingUnit == 'F':
            self.ceilingUnit = 'FT'
        self.ceilingRef = xmlAirspace.find('ALTLIMIT_TOP').get('REFERENCE')
        self.floor = xmlAirspace.find('ALTLIMIT_BOTTOM').findtext('ALT')
        self.floorUnit = xmlAirspace.find('ALTLIMIT_BOTTOM').find('ALT').get('UNIT')
        if self.floorUnit == 'F':
            self.floorUnit = 'FT'
        self.floorRef = xmlAirspace.find('ALTLIMIT_BOTTOM').get('REFERENCE')
        self.lng, self.lat = self.__getCoordinates(xmlAirspace)

    def toSQL(self, cursor, id, cId):
        '''Write to SQLite database
        '''
        cursor.execute('INSERT INTO Airspaces VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
            (id,
            cId,
            self.name,
            self.category,
            self.ceiling,
            self.ceilingUnit,
            self.ceilingRef,
            self.floor,
            self.floorUnit,
            self.floorRef,
            self.lat,
            self.lng))
        
    def write(self):
        '''Print data to console
        '''
        print '--- Airspace ---'
        print 'Country:', self.country
        print 'Name:', self.name
        print 'Category:', self.category
        print 'Vertical limits:', self.ceiling, self.ceilingUnit, self.ceilingRef, '-', self.floor, self.floorUnit, self.floorRef
        print 'Lateral limits (latitude):', self.lat
        print 'Lateral limits ()longitude):', self.lng
        
    def __getCoordinates(self, xmlAirspace):
        '''Parse airspace coordinates
        '''
        lng = ''
        lat = ''
        if xmlAirspace.find('GEOMETRY')[0].tag == 'POLYGON': # TODO implement other type of geometry?
            polydata = xmlAirspace.find('GEOMETRY').findtext('POLYGON').split(',')
            for coord in polydata:
                x, y = coord.lstrip().split(' ', 1)
                lng += x + ','
                lat += y + ','
        else:
            raise RuntimeError('Expected to find POLYGON in GEOMETRY object from airspace data, but found', xmlAirspace.find('GEOMETRY')[0].tag, 'instead!\n')
        return lng[:-1], lat[:-1]
        
