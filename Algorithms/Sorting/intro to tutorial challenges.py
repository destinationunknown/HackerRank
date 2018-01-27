'''input
4
6
1 4 5 7 9 12
'''

#!/bin/python

import sys

def introTutorial(V, arr):
	print arr.index(V)

if __name__ == "__main__":
	V = int(raw_input().strip())
	n = int(raw_input().strip())
	arr = map(int, raw_input().strip().split(' '))
	introTutorial(V, arr)