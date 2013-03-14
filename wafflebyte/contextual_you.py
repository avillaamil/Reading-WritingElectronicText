import sys
import re

for line in sys.stdin:
  line = line.strip()
  for matching_string in re.findall(r'\b[Ii]kea \w+', line):
    print matching_string

