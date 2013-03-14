import sys
import re

for line in sys.stdin:
  line = line.strip()
  # if re.search(r'\b\w+\s\b[Ii]kea\b\s\w+\b', line):
  #if re.search(r'\w+ [Ii]kea \w+', line):
  #if re.search(r'\b\w+\b[Ii]kea \w+', line):
  #if re.search(r'\w+\b[Ii]kea \w+', line):
  if re.search(r'\w\w [Ii]kea \w+ \b', line):

    print line

