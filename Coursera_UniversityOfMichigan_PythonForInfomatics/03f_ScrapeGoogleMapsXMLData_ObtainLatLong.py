# script to take a geographical location, access google maps
# and return the lat-long associated with that location

import urllib
import xml.etree.ElementTree as ET

# Google maps api
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

# loop to access api and obtain lat-long
while True:
    # enter the location you want the co-ords for
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location