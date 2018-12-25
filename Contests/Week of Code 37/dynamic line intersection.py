'''input
4
+ 1 0
+ 2 0
? 2 
? 1
'''

#!/bin/python

import os
import sys



def dynamicLineIntersection(n):
	lines = []
	for t in xrange(n):
		query = str(raw_input())
		inter = 0

		if query[0] == "+":
			k, b = query[1:].split()
			lines.append([int(k), int(b)])

		if query[0] == "-":
			k, b = query[1:].split()
			#lines.remove([int(k), int(b)])
			lines = [x for x in lines if [int(k), int(b)]]

		if query[0] == "?":
			q = int(query[1:])
			for line in lines:
				if (q-line[1]) % line[0] == 0:
					inter += 1

			print inter

if __name__ == '__main__':
	
	n = int(raw_input())

	dynamicLineIntersection(n)