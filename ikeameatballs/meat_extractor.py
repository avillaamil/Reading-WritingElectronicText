import sys


meatball_set = set()
# look at this document for word extractors
for line in open('meatballs.txt'):

  # strip the lines of carriage returns etc
  line = line.strip()
  # add this data to the set
  meatball_set.add(line)

# for all the lines in standard input (this provided text)
for line in sys.stdin:
  line = line.strip()
  words = [x for x in line.split(" ") if x.lower() in meatball_set]
  if len(words) > 0:

  




    print ' '.join(words)

