#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et
import math

## Navaid
#  Manage navigational aid data
#
#  Adrien Crovato
class Navaid:
    def __init__(self, xmlNavaid):
        self.country = xmlNavaid.findtext('COUNTRY')
        self.name = xmlNavaid.findtext('NAME')
        self.type = xmlNavaid.get('TYPE')
        self.callsign = xmlNavaid.findtext('ID')
        self.latitude = xmlNavaid.find('GEOLOCATION').findtext('LAT')
        self.longitude = xmlNavaid.find('GEOLOCATION').findtext('LON')
        self.elevation = xmlNavaid.find('GEOLOCATION').findtext('ELEV')
        self.elevationUnit = xmlNavaid.find('GEOLOCATION').find('ELEV').get('UNIT')
        if self.elevationUnit == 'M': # to feet
            self.elevation = int(math.ceil(float(self.elevation) * 3.2808399))
            self.elevationUnit = 'FT'
        self.latitude = round(float(self.latitude), 2)
        self.longitude = round(float(self.longitude), 2)
        self.frequency = xmlNavaid.find('RADIO').findtext('FREQUENCY')
        self.channel = xmlNavaid.find('RADIO').findtext('CHANNEL')
        self.range = xmlNavaid.find('PARAMS').findtext('RANGE')
        self.rangeUnit = xmlNavaid.find('PARAMS').find('RANGE').get('UNIT')
        self.declination = xmlNavaid.find('PARAMS').findtext('DECLINATION')
        self.trueNorth = xmlNavaid.find('PARAMS').findtext('ALIGNEDTOTRUENORTH')

    def toSQL(self, cursor, id, cId):
        '''Write to SQLite database
        '''
        cursor.execute('INSERT INTO Navaids VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (id,
            cId,
            self.name,
            self.type,
            self.callsign,
            self.latitude,
            self.longitude,
            self.elevation,
            self.elevationUnit,
            self.frequency,
            self.channel,
            self.range,
            self.rangeUnit))
        
    def write(self):
        '''Print data to console
        '''
        print '--- Navaid ---'
        print 'Country:', self.country
        print 'Name:', self.name
        print 'Type:', self.type
        print 'Callsign:', self.callsign
        print 'Frequency:', self.frequency
        print 'Channel:', self.channel
        print 'Range:', self.range, self.rangeUnit
        print 'Latitude:', self.latitude
        print 'Longitude:', self.longitude
        print 'Elevation:', self.elevation, self.elevationUnit
        print 'Declination:', self.declination
        print 'Aligned to true North:', self.trueNorth
