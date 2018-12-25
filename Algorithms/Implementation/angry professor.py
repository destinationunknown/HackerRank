### SOLVED ###

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.


def angryProfessor(k, a):
    onTimeCount = 0

    for x in a:
        if x <= 0:
            onTimeCount += 1

    if onTimeCount >= k:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nk = raw_input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = map(int, raw_input().rstrip().split())

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
