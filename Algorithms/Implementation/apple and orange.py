'''input
7 11
5 15
3 2
-2 2 1
5 -6
'''

#!/bin/python

import sys

def appleAndOrange(s, t, a, b, apples, oranges):
	print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
	print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))


if __name__ == "__main__":
	s, t = raw_input().strip().split(' ')
	s, t = [int(s), int(t)]
	a, b = raw_input().strip().split(' ')
	a, b = [int(a), int(b)]
	m, n = raw_input().strip().split(' ')
	apple = map(int, raw_input().strip().split(' '))
	orange = map(int, raw_input().strip().split(' '))
	appleAndOrange(s, t, a, b, apple, orange)
