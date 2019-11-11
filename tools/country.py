#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et
import airport as apt
import airspace as aps
import navaid as nva

## Country
#  Manage country data
#
#  Adrien Crovato
class Country:
    def __init__(self, xmlpath, name, code):
        self.path = xmlpath
        self.name = name.capitalize()
        self.code = code.upper()
        self.airports = self.__getAirports()
        self.airspaces = self.__getAirspaces()
        self.navaids = self.__getNavaids()
        
    def toSQL(self, cursor, id):
        '''Write to SQLite database
        '''
        cursor.execute('INSERT INTO Countries VALUES (?,?,?)', (id, self.name, self.code))
        
    def write(self):
        '''Print data to console
        '''
        print '--- Country ---'
        print 'Name:', self.name
        print 'Code:', self.code
        for airport in self.airports:
            airport.write()
        for airspace in self.airspaces:
            airspace.write()
        for navaid in self.navaids:
            navaid.write()

    def __getAirports(self):
        '''Get airports data from XML
        '''
        import os
        print 'Creating airports of', self.name, '...'
        fxml = os.path.join(self.path, 'openaip_airports' + '_' + self.name.lower() + '_' + self.code.lower() + '.aip')
        tree = et.parse(fxml)
        root = tree.getroot()
        airports = []
        for xmlAirport in root[0]:
            airports.append(apt.Airport(xmlAirport))
        return airports
        
    def __getAirspaces(self):
        '''Get airspaces data from XML
        '''
        import os
        print 'Creating airspaces of', self.name, '...'
        fxml = os.path.join(self.path, 'openaip_airspace' + '_' + self.name.lower() + '_' + self.code.lower() + '.aip')
        tree = et.parse(fxml)
        root = tree.getroot()
        airspaces = []
        for xmlAirspace in root[0]:
            airspaces.append(aps.Airspace(xmlAirspace))
        return airspaces
        
    def __getNavaids(self):
        '''Get navaids data from XML
        '''
        import os
        print 'Creating navaids of', self.name, '...'
        fxml = os.path.join(self.path, 'openaip_navaid' + '_' + self.name.lower() + '_' + self.code.lower() + '.aip')
        tree = et.parse(fxml)
        root = tree.getroot()
        navaids = []
        for xmlNavaid in root[0]:
            navaids.append(nva.Navaid(xmlNavaid))
        return navaids
