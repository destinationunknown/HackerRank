'''input
6
'''

#!/bin/python

import sys

def staircase(n):
	for i in xrange(1, (n + 1)):
		for j in xrange(0, n-i):
			sys.stdout.write(" ")
		for k in xrange(0, i):
			 sys.stdout.write("#")
		sys.stdout.write("\n")

if __name__ == "__main__": 
	n = int(raw_input().strip())
	staircase(n)
