'''input
10
0 1 1 0 1 1 1 1 0 0
'''

#!/bin/python

import sys

def revisedRussianRoulette(doors):
	maxCount = doors.count(1)
	minCount = 0

	i = 0
	for door in doors:
		if door == 1:
			if i == len(doors)-1:
				doors[i] = 0
				minCount += 1
			else:
				doors[i] = 0
				doors[i+1] = 0
				minCount += 1
		i += 1

	return str(minCount) + ' ' + str(maxCount)

if __name__ == "__main__":
	n = int(raw_input().strip())
	doors = map(int, raw_input().strip().split(' '))
	result = revisedRussianRoulette(doors)
	print result
