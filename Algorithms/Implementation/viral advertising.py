### SOLVED ###

#!/bin/python

import math
import os
import random
import re
import sys


def viralAdvertising(n):

    shared = 5
    liked = 0
    cumulative = 0

    for i in range(n):
        liked = math.floor(shared/2)
        cumulative += liked
        shared = liked * 3

    return int(cumulative)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
