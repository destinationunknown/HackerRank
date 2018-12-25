'''input
5
84
92
61
50
95
'''

#!/bin/python
from __future__ import print_function

import os
import sys
from decimal import Decimal, ROUND_HALF_UP

def averageOfTopEmployees(rating):
	#r
	average = 0.0
	count = 0

	for rat in rating:
		if rat >= 90 and rat <= 100:
			average += rat
			count += 1

	average = Decimal(average/count + 0.0005).quantize(Decimal("0.01"), ROUND_HALF_UP)

	print (average)


if __name__ == '__main__':
    n = int(raw_input())

    rating = []

    for _ in xrange(n):
        rating_item = int(raw_input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)