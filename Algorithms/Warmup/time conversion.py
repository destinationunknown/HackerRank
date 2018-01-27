'''input
12:05:39PM
'''

#!/bin/python

import sys

def timeConversion(s):
	if s[-2:] == "AM":
		if s[:2] == "12":
			return "00" + s[2:8]
		else:
			return s[:8]
	if s[-2:] == "PM":
		if s[:2] == "12":
			return "12" + s[2:8]
		else:
			hrs = str(int(s[:2]) + 12)
			return hrs + s[2:8]

s = raw_input().strip()
result = timeConversion(s)
print(result)