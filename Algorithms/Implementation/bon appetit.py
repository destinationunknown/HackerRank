'''input
4 1
3 10 2 9
7
'''

#!/bin/python

# https://www.hackerrank.com/challenges/bon-appetit/problem

import sys

def bonAppetit(n, k, b, ar):
	ar.remove(ar[k])
	cost = sum(ar)/2

	if cost-b == 0:
		return "Bon Appetit"
	else:
		return str(b-cost)


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print result
