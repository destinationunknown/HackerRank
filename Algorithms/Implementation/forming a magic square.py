'''input
4 8 2
4 5 7
6 1 6
'''

#!/bin/python

import sys

def formingMagicSquare(s):
	squares = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[6, 1, 8], [7, 5, 3], [2, 9, 4]], [[4, 9, 2], [3, 5, 7], [8, 1, 6]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]],  [[8, 3, 4], [1, 5, 9], [6, 7, 2]], [[4, 3, 8], [9, 5, 1], [2, 7, 6]], [[6, 7, 2], [1, 5, 9], [8, 3, 4]], [[2, 7, 6], [9, 5, 1], [4, 3, 8]],]

	totals = []

	for sq in squares:
		total = 0
		
		for row in sq:
			for i in row:
				j = s[sq.index(row)][row.index(i)]
				if i != j:
					total += abs(i-j)

		totals.append(total)

	return min(totals)
 
if __name__ == "__main__":
	s = []
	for s_i in xrange(3):
		s_temp = map(int, raw_input().strip().split(' '))
		s.append(s_temp)

	result = formingMagicSquare(s)
	print result