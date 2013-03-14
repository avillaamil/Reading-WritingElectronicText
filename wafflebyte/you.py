import sys
import re

for line in sys.stdin:
  line = line.strip()
  if re.search(r'\b[Ii]kea\b', line):
    print line

