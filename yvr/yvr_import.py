#!/usr/bin/python

# This script will read street_intersections.json and import the data into a postgresql database.

import json
import psycopg2
from pyproj import Proj, transform

yvr_data = '/home/khalid/Development/intersection_import/yvr/street_intersections.json'
dbConn = psycopg2.connect("host='localhost' dbname='intersections' user='postgres' password='moo'")

# Set spatial reference units to be used.
inputSRS = Proj(init='epsg:26910')
outputSRS = Proj(init='epsg:4326')

# Open JSON data file
with open(yvr_data) as json_file:
    data = json.load(json_file)
    dbCur = dbConn.cursor()

    # Iterate through JSON and gather intersection information
    for intersections in data['features']:

        # Convert spatial data from JSON data to format usable by Google and save to database
        longitude, latitude = transform(inputSRS, outputSRS, intersections['geometry']['coordinates'][0], intersections['geometry']['coordinates'][1])
        dbCur.execute("insert into yvr_data (coordinate1, coordinate2, intersection_name, latitude, longitude) values (%s, %s, %s, %s, %s)", [ intersections['geometry']['coordinates'][0], intersections['geometry']['coordinates'][1], intersections['properties']['XSTREET'], latitude, longitude ])
    dbConn.commit()
dbCur.close()
dbConn.close()
