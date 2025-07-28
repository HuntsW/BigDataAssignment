#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = str(line).strip()
    words = re.split(r"\W+", line)
    for word in words:
        if len(word)>0:
            print('%s\t%s' % (word, 1))
