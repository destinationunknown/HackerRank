'''input
5
1 2 1 3 2
3 2
'''



#!/bin/python

import sys

def solve(n, s, d, m):
	count = 0
	index = 0
	for piece in s:
		if sum(s[index:(index+(m))]) == d:
			count += 1
		
		index += 1
	print count

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
solve(n, s, d, m)