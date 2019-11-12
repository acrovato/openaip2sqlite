# openaip2sqlite
Python utilities to convert [openAIP](http://www.openaip.net/) data to SQLite

## Requirements
Python 2.7 (with the xml.etree and sqlite3 standard packages).  
Tested with python 2.7.8 on windows 7 and python 2.7.15 on ubuntu18.04.  

## Usage
Open a terminal/command prompt and run
```
python run.py path/to/source [--verbose]
```
Where `path/to/source` is the relative path to the directory where the openAIP files are. Currently supported input formats:
- [x] XML
- [ ] cup
- [ ] dat
 
The resulting database file will be located under `sqlite/world.db`.

## Doc
Tables in the database:  
- Countries
  - id `PRIMARY KEY INTEGER`
  - name `TEXT`
  - code `TEXT`
- Airports
  - id `PRIMARY KEY INTEGER`
  - countryId `FOREIGN KEY INTEGER` (references `id` of Countries entry)
  - name `TEXT`
  - icao `TEXT`
  - type `TEXT`
  - country `TEXT`
  - latitude `REAL`
  - longitude `REAL`
  - elevation `INTEGER`
  - elevationUnit `TEXT`
- Airspaces
  - id `PRIMARY KEY INTEGER`
  - countryId `FOREIGN KEY INTEGER` (references `id` of Countries entry)
  - name `TEXT`
  - category `TEXT`
  - ceiling `TEXT`
  - ceilingUnit `TEXT`
  - ceilingRef `TEXT` (altimetry: height, altitude, flight level)
  - floor `TEXT`
  - floorUnit `TEXT`
  - floorRef `TEXT` (altimetry: height, altitude, flight level)
  - lat `TEXT` (comma-separated values of latitude perimeter points)
  - lng `TEXT` (comma-separated values of longitude perimeter points)
- Navaids
  - id `PRIMARY KEY INTEGER`
  - countryId `FOREIGN KEY INTEGER` (references `id` of Countries entry)
  - name `TEXT`
  - type `TEXT` (ndb, vor, ...)
  - callsign `TEXT`
  - latitude `REAL`
  - longitude `REAL`
  - elevation `INTEGER`
  - elevationUnit `TEXT`
  - frequency `TEXT`
  - channel `TEXT`
  - range `TEXT`
  - rangeUnit `TEXT`
- Runways
  - id `PRIMARY KEY INTEGER`
  - airportId `FOREIGN KEY INTEGER` (references `id` of Airports entry)
  - name `TEXT`
  - surface `TEXT`
  - length `INTEGER`
  - lengthUnit `TEXT`
  - width `INTEGER`
  - widthUnit `TEXT`
- Frequencies
  - id `PRIMARY KEY INTEGER`
  - airportId `FOREIGN KEY INTEGER` (references `id` of Airports entry)
  - callsign `TEXT`
  - frequency `TEXT`
  - category `TEXT` (communication, navigation, ...)
  - type `TEXT` (tower, ground, ...)
