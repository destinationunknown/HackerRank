'''input
4
3 2 1 3
'''

#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
	maxnum = 0
	maxcount = 0
	for num in ar:
		if num == maxnum:
			maxcount += 1

		if num > maxnum:
			maxnum = num
			maxcount = 1
		
	return str(maxcount)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)