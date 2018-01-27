'''input
10 2 3
3 1
5 2 8
'''

#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
	if min(keyboards) + min(drives) > s:
		return str(-1)

	maxCost = 0

	for keyboard in keyboards:
		for drive in drives:
			if keyboard + drive <= s and keyboard + drive >= maxCost:
				maxCost = keyboard + drive

	return str(maxCost)

s, n, m = raw_input().strip().split(' ')
s, n, m = [int(s), int(n), int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
moneySpent = getMoneySpent(keyboards, drives, s)
print moneySpent