import urllib
from BeautifulSoup import *

# script to go to a webpage and
# follow links present on the page

#url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/known_by_Darrach.html"

# Set the position of the first link
pos = int(raw_input("What number link do you want?: "))
pos = pos -1

# Set the number of times you want to repeat this process
# i.e. How many links should we click?
iter = int(raw_input("How many times should we iterate?: "))

# loop that will go to the link1 and print it
# the loop will now travel from link1 to link2 etc.
for i in range(iter):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    link = tags[pos].get("href", None)
    print link
    url = link

