'''input
6
31415926535897932384626433832795
1
3
10
3
5
'''

#!/bin/python

import sys

def bigSorting(arr):
	isSorted = False

	for s in sorted(arr, key=int):
		print s

if __name__ == "__main__":
	n = int(raw_input().strip())
	arr = []
	arr_i = 0
	for arr_i in xrange(n):
		arr_t = str(raw_input().strip())
		arr.append(arr_t)
	bigSorting(arr)
	