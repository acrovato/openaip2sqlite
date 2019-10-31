#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et
import runway as rwy
import frequency as frq
import math

## Airport
#  Manage airport data
#
#  Adrien Crovato
class Airport:
    def __init__(self, xmlAirport):
        self.country = xmlAirport.findtext('COUNTRY')
        self.name = xmlAirport.findtext('NAME')
        self.icao = xmlAirport.findtext('ICAO')
        self.latitude = xmlAirport.find('GEOLOCATION').findtext('LAT')
        self.longitude = xmlAirport.find('GEOLOCATION').findtext('LON')
        self.elevation = xmlAirport.find('GEOLOCATION').findtext('ELEV')
        self.elevationUnit = xmlAirport.find('GEOLOCATION').find('ELEV').get('UNIT')
        if self.elevationUnit == 'M': # to feet
            self.elevation = math.ceil(float(self.elevation) * 3.2808399)
            self.elevationUnit = 'FT'
        self.runways = self.__getRunways(xmlAirport)
        self.frequencies = self.__getFrequencies(xmlAirport)

    def toSQL(self, cursor, id, cId):
        '''Write to SQLite database
        '''
        cursor.execute('INSERT INTO Airports VALUES (?,?,?,?,?,?,?,?)',
            (id,
            cId,
            self.name,
            self.icao,
            self.latitude,
            self.longitude,
            self.elevation,
            self.elevationUnit))

    def write(self):
        '''Print data to console
        '''
        print '--- Airport ---'
        print 'Country:', self.country
        try:
            print 'Name:', self.name
        except:
            pass
        print 'ICAO:', self.icao
        print 'Latitude:', self.latitude
        print 'Longitude:', self.longitude
        print 'Elevation:', self.elevation, self.elevationUnit
        for runway in self.runways:
            runway.write()
        for frequency in self.frequencies:
            frequency.write()
        
    def __getRunways(self, xmlAirport):
        '''Get runways data from XML
        '''
        runways = []
        for xmlRunway in xmlAirport.findall('RWY'):
            runways.append(rwy.Runway(xmlRunway))
        return runways
    
    def __getFrequencies(self, xmlAirport):
        '''Get frequencies data from XML
        '''
        frequencies = []
        for xmlFrequency in xmlAirport.findall('RADIO'):
            frequencies.append(frq.Frequency(xmlFrequency))
        return frequencies
