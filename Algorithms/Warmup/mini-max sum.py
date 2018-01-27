'''input
1 2 3 4 5
'''

#!/bin/python

import sys

def miniMaxSum(arr):
	max = 0
	min = 10000000000
	for num in arr:
		currentsum = sum(arr) - num
		if currentsum > max:
			max = currentsum
		if currentsum < min:
			min = currentsum

	sys.stdout.write(str(min) + " " + str(max))

if __name__ == "__main__":
	arr = map(int, raw_input().strip().split(' '))
	miniMaxSum(arr)
