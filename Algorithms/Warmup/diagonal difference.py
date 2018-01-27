#!/bin/python

# Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference
# Status - Accepted

import sys

def diagonalDifference(a):
    prim = 0
    secon = 0
    rowcount = 0

    for row in a:
    	prim += row[rowcount]
    	secon += row[len(row) - (rowcount + 1)]
    	rowcount += 1
    return abs(prim - secon)

if __name__ == "__main__": 
	n = int(raw_input().strip())
	a = []
	for a_i in xrange(n):
	    a_temp = map(int,raw_input().strip().split(' '))
	    a.append(a_temp)
	result = diagonalDifference(a)
	print result