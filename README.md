# intersection_import
This repository contains python scripts used to generate a database of google street view images of street intersections from various cities. Each sub-folder contains data for a specific city. All intersection and image data will be stored in a folder on the filesystem. Each intersection will have 4 images saved - north, east, south, west, with a 120-degree field of view.

YVR
===

Vancouver intersection source data from http://data.vancouver.ca/datacatalogue/cityStreets.htm. The data file uses the EPSG 26910 coordinate system, which requires conversion to WGS84 coordinate system for use with Google Maps and Street View.