'''input
9
10 20 20 10 10 30 50 10 20
'''


#!/bin/bash

import sys
from collections import Counter


def sockMerchant(n, ar):
	sock = 0
	count = dict(Counter(ar))

	for elem in count:
		sock += count[elem]/2

	print sock

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
sockMerchant(n, ar)


