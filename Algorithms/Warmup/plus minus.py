'''input
6
-4 3 -9 0 4 1
'''

#!/bin/python

# Plus Minus
# https://www.hackerrank.com/challenges/plus-minus/problem
# Status - Accepted

from __future__ import division
import sys

def plusMinus(arr, n):
    pos = 0 
    neg = 0
    zero = 0
    for num in arr:
    	if num > 0:
    		pos += 1
    	if num == 0:
    		zero += 1
    	if num < 0:
    		neg += 1

    print pos/n
    print neg/n
    print zero/n


if __name__ == "__main__":
	n = int(raw_input().strip())
	arr = map(int, raw_input().strip().split(' '))
	plusMinus(arr, n)