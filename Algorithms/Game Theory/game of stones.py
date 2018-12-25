'''input
8
1
2
3
4
5
6
7
10
'''

#!/bin/python

import sys

def gameOfStones(n):
	if n == 1:
		return "Second"

	elif n <= 5:
		return "First"
	elif n % 2 is not 0 and n % 3 is not 0:
		return "Second"
	else:
		return "First"

if __name__ == "__main__":
	t = int(raw_input().strip())
	for a0 in xrange(t):
		n = int(raw_input().strip())
		result = gameOfStones(n)
		print result