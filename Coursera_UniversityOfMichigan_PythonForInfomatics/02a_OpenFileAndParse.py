# prompt for file name
fname = raw_input("Enter file name: ")

# hit enter to go straight to the default file
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

# for loop to iterate throught the text file
# and locate where a line starts with "From"
for line in fh:
    if line.startswith('From'):
        if not line.startswith('From:'):
            count += 1
            line = line.split()
            line = line[1]

print "There were %d lines with From as the first word" %count

