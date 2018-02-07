'''input
6
5
'''

#!/bin/python

import sys

def solve(n, p):
	if p < n/2 + 1 :
		return p/2
	if n-p == 1:
		return 1
	else:
		return (n-p)/2 


n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print result