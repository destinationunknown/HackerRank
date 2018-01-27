'''input
1 1
1
100
'''

#/bin/python

import sys

def getTotalX(a, b):
	
	total = 0

	for x in range(max(a), (min(b) + 1)):
		isValid = True
		for num in b:
			if num != 0 and x != 0:
				if num % x != 0:
					isValid = False
		if isValid:
			for num in a:
				if num != 0 and x != 0:
					if x % num != 0:
						isValid = False

			if isValid:
				total += 1

	return total

if __name__ == "__main__":
	n, m = raw_input().strip().split(' ')
	n, m = [int(n), int(m)]
	a = map(int, raw_input().strip().split(' '))
	b = map(int, raw_input().strip().split(' '))
	total = getTotalX(a, b)
	print total
