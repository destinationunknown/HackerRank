'''input
0 2 5 3
'''

#!/bin/python

import sys


def kangaroo(x1, v1, x2, v2):
	
	if x1 > x2 and v1 >= v2:
		return "NO"
	elif x2 > x1 and v2 >= v1:
		return "NO"
	else:
		if (x1 - x2) % (v2 - v1) == 0:
			return "YES"
		else:
			return "NO"

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)