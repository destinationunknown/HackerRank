'''input
3
1 2 3
1 3 2
2 1 3
'''

#1/bin/bash

import sys 

def catAndMouse(x, y, z):
	if abs(x - z) < abs(y - z):
		print "Cat A"
	elif abs(x - z) > abs(y - z):
		print "Cat B"
	elif abs(x - z) == abs(y - z):
		print "Mouse C"


if __name__ == "__main__":
	q =int(raw_input().strip())
	for a0 in xrange(q):
		x, y, z = raw_input().strip().split(' ')
		x, y, z = [int(x), int(y), int(z)]
		catAndMouse(x, y , z)