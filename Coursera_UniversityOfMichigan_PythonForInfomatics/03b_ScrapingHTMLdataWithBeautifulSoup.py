# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# into the same folder as this program

# module imports
# BeautifulSoup makes parsing web data much easier
import urllib
from BeautifulSoup import *

# prompt for url
#url = raw_input('Enter - ')

# Hardcode the url for testing purposes
# The file is 2 columns:
#  column a = User name
# column b = Number of comments by that user

url = 'http://python-data.dr-chuck.net/comments_42.html'

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all the anchor tags
tags = soup('span')

# extract the number of comments from the tag
print tags[0].contents

sum = 0

# iterate through the tags and find the total number of comments
for tag in tags:
    count = tag.contents[0]
    sum += int(count)
print "The sum of all the comments is: ", sum
