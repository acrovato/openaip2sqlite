#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et
import country as ctr
import airport as apt
import airspace as aps
import navaid as nva

## Manager
#  Manage general operations
#
#  Adrien Crovato
class Manager:
    def __init__(self, xmlpath):
        self.path = xmlpath

    def run(self):
        '''Parse XMLs, create data structure and write database
        '''
        self.__checkDB()
        countries = self.__getCountries()
        for country in countries:
            country.write()
            airports = self.__getAirports(country)
            for airport in airports:
                airport.write()
            airspaces = self.__getAirspaces(country)
            for airspace in airspaces:
                airspace.write()
            navaids = self.__getNavaids(country)
            for navaid in navaids:
                navaid.write()
                
    def __checkDB(self):
        '''Check that database exists and update it if necessary
        '''
        import os
        # TODO update instead of delete to create again
        if os.path.isfile(os.path.join(os.getcwd(), 'world.db')):
            print 'Removing database:', os.path.join(os.getcwd(), 'world.db')
            os.remove(os.path.join(os.getcwd(), 'world.db'))
        print 'Creating database:', os.path.join(os.getcwd(), 'world.db'), '...'

    def __getCountries(self):
        '''Find the countries and check that data are present
        '''
        import os
        aptcnt = 0
        apscnt = 0
        navcnt = 0
        countries = []
        for entry in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, entry)):
                split = entry.split('_')
                if split[1] == 'airports':
                    aptcnt +=1
                    countries.append(ctr.Country(split[2], split[3][:-4]))
                elif split[1] == 'airspace':
                    apscnt +=1
                elif split[1] == 'navaid':
                    navcnt +=1
                else:
                    raise RuntimeError('Unrecognized type of openAIP file: ' + entry + '!\n')
        if (aptcnt == apscnt and apscnt == navcnt):
            return countries
        else:
            raise RuntimeError('Some data files are missing, counted {0} airports, {1} airspaces, and {2} navaids files!\n'.format(aptcnt, apscnt, navcnt))

    def __getAirports(self, country):
        '''Get airports data from XML
        '''
        import os
        fxml = os.path.join(self.path, 'openaip_airports' + '_' + country.name + '_' + country.code + '.aip')
        tree = et.parse(fxml)
        root = tree.getroot()
        airports = []
        for xmlAirport in root[0]:
            airports.append(apt.Airport(xmlAirport))
        return airports
        
    def __getAirspaces(self, country):
        '''Get airspaces data from XML
        '''
        import os
        fxml = os.path.join(self.path, 'openaip_airspace' + '_' + country.name + '_' + country.code + '.aip')
        tree = et.parse(fxml)
        root = tree.getroot()
        airspaces = []
        for xmlAirspace in root[0]:
            airspaces.append(aps.Airspace(xmlAirspace))
        return airspaces
        
    def __getNavaids(self, country):
        '''Get navaids data from XML
        '''
        import os
        fxml = os.path.join(self.path, 'openaip_navaid' + '_' + country.name + '_' + country.code + '.aip')
        tree = et.parse(fxml)
        root = tree.getroot()
        navaids = []
        for xmlNavaid in root[0]:
            navaids.append(nva.Navaid(xmlNavaid))
        return navaids
