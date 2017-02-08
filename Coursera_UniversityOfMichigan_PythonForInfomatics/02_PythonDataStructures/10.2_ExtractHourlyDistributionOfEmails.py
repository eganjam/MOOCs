# prompt for the file
fname = raw_input("Enter file name: ")

# press enter to use the default file
if len(fname) < 1 : fname = "mbox-short.txt"

# open the file
fh = open(fname)
count = 0
counts = {}

# for loop to go through each email and extract
# the hour in which that email was sent
for line in fh:
    if line.startswith('From'):
        if not line.startswith('From:'):
            count += 1
            line = line.split()
            #print line
            line = line[5]
            line = line.split(":")
            hour = line[0]

            counts[hour] = counts.get(hour, 0) + 1

#print counts.items()

lst = list()

for key, val in counts.items():

    lst.append((key,val))

lst.sort(reverse = False)

# list the hour and the number of emails sent
for val,key in lst:
   print "Hour: %s   Emails sent: %s" %(val, key)
