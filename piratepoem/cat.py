# our very first program

# import tells python that it needs to use a specific library -> sys
# sys is the library for interacting with the command line
# line has the input on the right
# we're iterating over every line of input from the user
# strip method takes the string and strips out all whitespace from end of string
# then print that line back out to standard output

import sys
for line in sys.stdin:
	line = line.strip()
	print line
