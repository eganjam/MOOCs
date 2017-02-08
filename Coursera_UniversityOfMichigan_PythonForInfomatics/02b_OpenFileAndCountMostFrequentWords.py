# script to open a file and extract the most frequent word

name = raw_input("Enter file: ")

# upon prompt press enter to use the mbox file
if len(name) == 0:
    name = "mbox-short.txt"

# use try and except as a failsafe
try:
    handle = open(name)
except:
    print "This file cannot be opened"
    exit()

# read the text
text = handle.read()

# extract the words
words = text.split()

# create an empty dictionary
counts = {}

# for loop that will iterate through the text and add 1
# to the word value every time it is encountered
for word in words:
    counts[word] = counts.get(word,0)+1

#print counts

#print counts.items()


# now let's find which word is the most frequent in this text
max_val = 0

max_key = None

for key, val in counts.items():

    if val > max_val:
        max_val = val
        max_key = key

print max_key, max_val