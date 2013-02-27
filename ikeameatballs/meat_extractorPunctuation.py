import sys


meatball_set = set()
punctuation_set = set()
punctuationList = list()

# look at this document for word extractors
for line in open('meatballs.txt'): 
  line = line.strip()
  # add this data to the set
  meatball_set.add(line)

# look at this document for punctuation
for this in open('punctuation.txt'): 
  this = this.strip()
  # add this data to the set
  punctuation_set.add(this)

# for all the lines in standard input (this provided text)
for line in sys.stdin:
  line = line.strip()

  #punctuation = [x for x in line.split(" ") if x in punctuation_set]
  for x in line.split(" "):
  	if len(x)>0:
	  	if x[-1] in punctuation_set:
	  		punctuationList.append(x[-1])
  		  #punctuation = punctuation[-1]
  # last_letter = word[-1]
  # if last_letter in 

  words = [x for x in line.split(" ") if x.lower() in meatball_set]
  if len(punctuationList) > 0:
    print ' '.join(words)
   # print '\n'.join(punctuationList)


