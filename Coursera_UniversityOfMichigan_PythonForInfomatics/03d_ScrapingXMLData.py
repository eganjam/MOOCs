import urllib
import xml.etree.ElementTree as ET

# This script will scrape XML data and
# count the number of total number of comments made by each user
# The XML data is made of two columns
# column a = User name
# column b = Number of comments by that user

# hardcode the test website
url = 'http://python-data.dr-chuck.net/comments_294747.xml'

# open the url and read the file
xml = urllib.urlopen(url).read()

tree = ET.fromstring(xml)

# isolate the data we want
counts = tree.findall('.//count')

sum = 0

# loop through our comment counts and sum them
for element in counts:
    count = int(element.text)
    sum += count
print "The sum of all counts is: ", sum
