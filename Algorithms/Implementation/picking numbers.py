#!/bin/python

import sys

def pickingNumbers(a):
	a.sort()

	count = 0
	top = 0

	count_prev = a.count(1)


	for x in xrange(2 , max(a) + 1):
		count_curr = a.count(x)
		count = count_prev + count_curr
		
		if count > top:
			top = count


		count_prev = count_curr


	return top
	

if __name__ == "__main__":
	n = int(raw_input().strip())
	a = map(int, raw_input().strip().split(' '))
	result = pickingNumbers(a)
	print result
