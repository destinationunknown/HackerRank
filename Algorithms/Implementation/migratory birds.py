'''input
6
1 4 4 4 5 3
'''

#!/bin/python

import sys
from collections import Counter


def migratoryBirds(n, ar):
	max = 0
	maxID = 0

	count = dict(Counter(ar))

	for elem in sorted(count.iterkeys(), reverse=True):
		if count[elem] >= max:
			max = count[elem]
			maxID = elem

	print maxID

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
migratoryBirds(n, ar)