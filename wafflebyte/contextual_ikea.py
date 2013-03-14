import sys
import re

for line in sys.stdin:
  line = line.strip()
  for matching_string in re.findall(r'\w+\W \w+', line):
    print matching_string




  #if re.search(r'\w\w [Ii]kea \w+ \b', line):
  #for matching_string in re.findall(r'\w+\W \w+', line):     # this guy returns word, wordr
