'''input
5 7
2 5 4 5 2
'''

#!/bin/python

import sys

def hurdleRace(k, height):
	if k < max(height):
		print max(height) - k
	else:
		print 0

if __name__ == "__main__":
	n, k = raw_input().strip().split(' ')
	n, k = [int(n), int(k)]
	height = map(int, raw_input().strip().split(' '))
	hurdleRace(k, height)