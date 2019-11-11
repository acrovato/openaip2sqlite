#!/usr/bin/env python
# -*- coding: utf8 -*-

import sqlite3 as sql
import country as ctr

## Manager
#  Manage general operations
#
#  Adrien Crovato
class Manager:
    def __init__(self, xmlpath, _verbose):
        self.path = xmlpath
        self.verb = _verbose

    def run(self):
        '''Parse XMLs, create data structure and write database
        '''
        # get countries
        self.countries = self.__getCountries()
        if self.verb:
            for country in self.countries:
                country.write()
        # check and write to database
        self.__checkDB()
        self.__writeDB()

    def __getCountries(self):
        '''Find the countries and check that data are present
        '''
        import os
        print 'Creating countries...'
        aptcnt = 0
        apscnt = 0
        navcnt = 0
        countries = []
        for entry in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, entry)):
                split = entry.split('_')
                if split[1] == 'airports':
                    aptcnt += 1
                    countries.append(ctr.Country(self.path, split[2], split[3][:-4]))
                elif split[1] == 'airspace':
                    apscnt += 1
                elif split[1] == 'navaid':
                    navcnt += 1
                else:
                    raise RuntimeError('Unrecognized type of openAIP file: ' + entry + '!\n')
        if (aptcnt == apscnt and apscnt == navcnt):
            return countries
        else:
            raise RuntimeError('Some data files are missing, counted {0} airports, {1} airspaces, and {2} navaids files!\n'.format(aptcnt, apscnt, navcnt))

    def __checkDB(self):
        '''Check that database exists and update it if necessary
        '''
        import os
        # TODO update instead of delete to create again
        if os.path.isfile(os.path.join(os.getcwd(), 'world.db')):
            print 'Removing database:', os.path.join(os.getcwd(), 'world.db')
            os.remove(os.path.join(os.getcwd(), 'world.db'))
    
    def __writeDB(self):
        '''Create the SQLite database and add the parsed data
        '''
        import os
        # create db and open connection
        print 'Creating database:', os.path.join(os.getcwd(), 'world.db')
        conn = sql.connect('world.db')
        # create tables
        csr = conn.cursor()
        csr.execute('''CREATE TABLE Countries
             (id INTEGER PRIMARY KEY,
              name TEXT,
              code TEXT)''')
        csr.execute('''CREATE TABLE Airports
             (id INTEGER PRIMARY KEY,
              countryId INTEGER,
              name TEXT,
              icao TEXT,
              type TEXT,
              country TEXT,
              latitude REAL,
              longitude REAL,
              elevation INTEGER,
              elevationUnit TEXT,
              FOREIGN KEY (countryId) REFERENCES Countries (id)
              )''')
        csr.execute('''CREATE TABLE Runways
             (id INTEGER PRIMARY KEY,
              airportId INTEGER, 
              name TEXT,
              surface TEXT,
              length INTEGER,
              lengthUnit TEXT,
              width INTEGER,
              widthUnit TEXT,
              FOREIGN KEY (airportId) REFERENCES Airports (id)
              )''')
        csr.execute('''CREATE TABLE Frequencies
             (id INTEGER PRIMARY KEY,
              airportId INTEGER,
              callsign TEXT,
              frequency TEXT,
              category TEXT,
              type TEXT,
              FOREIGN KEY (airportId) REFERENCES Airports (id)
              )''')
        csr.execute('''CREATE TABLE Airspaces
             (id INTEGER PRIMARY KEY,
              countryId INTEGER,
              name TEXT,
              category TEXT,
              ceiling TEXT,
              ceilingUnit TEXT,
              ceilingRef TEXT,
              floor TEXT,
              floorUnit TEXT,
              floorRef TEXT,
              lat TEXT,
              lng TEXT,
              FOREIGN KEY (countryId) REFERENCES Countries (id)
              )''')
        csr.execute('''CREATE TABLE Navaids
             (id INTEGER PRIMARY KEY,
              countryId INTEGER,
              name TEXT,
              type TEXT,
              callsign TEXT,
              latitude REAL,
              longitude REAL,
              elevation INTEGER,
              elevationUnit TEXT,
              frequency TEXT,
              channel TEXT,
              range TEXT,
              rangeUnit TEXT,
              FOREIGN KEY (countryId) REFERENCES Countries (id)
              )''')
        # insert data
        ccnt = 0
        acnt = 0
        rcnt = 0
        fcnt = 0
        scnt = 0
        ncnt = 0
        for country in self.countries:
            country.toSQL(csr, ccnt)
            for airport in country.airports:
                airport.toSQL(csr, acnt, ccnt)
                for runway in airport.runways:
                    runway.toSQL(csr, rcnt, acnt)
                    rcnt += 1
                for frequency in airport.frequencies:
                    frequency.toSQL(csr, fcnt, acnt)
                    fcnt += 1
                acnt += 1
            for airspace in country.airspaces:
                airspace.toSQL(csr, scnt, ccnt)
                scnt += 1
            for navaid in country.navaids:
                navaid.toSQL(csr, ncnt, ccnt)
                ncnt += 1
            ccnt += 1
        # commit and close
        conn.commit() 
        conn.close()
