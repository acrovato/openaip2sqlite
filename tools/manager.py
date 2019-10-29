#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as et
import country as ctr
import airport as apt

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
                
    def __checkDB()
        '''Check that database exists and update it if necessary
        '''
        print 'oops'

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
                elif split[1] == 'airspaces':
                    apscnt +=1
                elif split[1] == 'navaids':
                    navcnt +=1
                else:
                    raise RuntimeError('Unrecognized type of openAIP file: ' + entry + '!\n')
                countries.append(ctr.Country(split[2], split[3][:-4]))
        if (aptcnt == apscnt and apscnt == navcnt):
            return countries
        else:
            return countries#raise RuntimeError('Some datafile are missing, counted {0} airports, {1} airspaces, and {2} navaids files!\n'.format(aptcnt, apscnt, navcnt))

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
