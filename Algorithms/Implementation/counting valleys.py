'''input
8
UDDDUDUU
'''

#!/bin/python

import sys

def countingValleys(n, s):
	inVal = False
	valCount = 0
	pos = 0
	for step in s:
		if step == 'U':
			pos += 1
		elif step == 'D':
			pos -= 1

		if pos == 0 and inVal == True:
			valCount += 1
		if pos < 0:
			inVal = True
		if pos > 0:
			inVal = False

	return valCount

if __name__ == "__main__":
	n = int(raw_input().strip())
	s = raw_input().strip()
	result = countingValleys(n, s)
	print result