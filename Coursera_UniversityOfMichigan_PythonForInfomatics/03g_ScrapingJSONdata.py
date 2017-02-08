import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_294751.json'

web_page = urllib.urlopen(url).read()

info = json.loads(web_page)

# Use this statement to see what data we are working with.
#print json.dumps(info, indent=4)

num_users = len(info["comments"])

## Loop through the json data and extract the counts

sum = 0

for i in range (num_users):
   count = info["comments"][i]["count"]
   sum  += count
print "The sum of the counts is: ", sum





