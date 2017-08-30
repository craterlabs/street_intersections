#!/usr/bin/python

# This script uses the yvr_data table to gather images from Google Street Views API and store them in the specified folder. 
# Images with north, east, south and west headings are saved in the database.

import requests
import psycopg2
import time
from PIL import Image
from io import BytesIO

google_api_key = ''

# Fetch image data from database
db = psycopg2.connect("host='localhost' dbname='intersections' user='postgres' password='moo'")
cursor = db.cursor()
cursor.execute("select * from yvr_data")
results = cursor.fetchall()

for r in results:
    direction = [45, 135, 225, 315]
    for x in direction:
        url = "https://maps.googleapis.com/maps/api/streetview?size=640x480&location=" + str(r[4]) + "," + str(r[5]) + "&fov=180&heading=" + str(x) + "&pitch=-5&key=" + google_api_key
        print url
        u = requests.get(url)
        img = Image.open(BytesIO(u.content))
        print (img.format, "%dx%d" % img.size, img.mode)
        image_name = "/u01/intersections/yvr_data/" + str(r[0]) + "_" + str(x) + ".jpg"
        img.save(image_name, "JPEG")
        time.sleep(1)
cursor.close()
db.close()




