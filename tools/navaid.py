#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et

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
        self.frequency = xmlNavaid.find('RADIO').findtext('FREQUENCY')
        self.channel = xmlNavaid.find('RADIO').findtext('CHANNEL')
        self.range = xmlNavaid.find('PARAMS').findtext('RANGE')
        self.rangeUnit = xmlNavaid.find('PARAMS').find('RANGE').get('UNIT')
        self.declination = xmlNavaid.find('PARAMS').findtext('DECLINATION')
        self.trueNorth = xmlNavaid.find('PARAMS').findtext('ALIGNEDTOTRUENORTH')

    def toSQL(self, fsql):
        '''Write to SQLite database
        '''
        print 'oops'
        
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
