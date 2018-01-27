'''input
6 3
1 3 2 6 1 12	
'''

#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
	count = 0
	index = 0
	for i in ar:
		for j in ar[index+1:]:
			if (i +j) % k == 0:
				count += 1

		index += 1 

	print count

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
divisibleSumPairs(n, k, ar)