#!/usr/bin/env python

import sys

print 'Running mapper'

for line in sys.stdin:
	# Removes leading and trailing spaces
	Line = line.strip()
	# split the words in the line
	words = line.split()
	for word in words:
		print '%s %s' %(word,1)

	
