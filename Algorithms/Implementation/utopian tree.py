#!/bin/python

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
	height = 1

	for x in xrange(1, n+1):
		if (x % 2 != 0): 
			height = height * 2
		else:
			height += 1
	
	return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()