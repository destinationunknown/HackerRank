'''input
3
add -5
set 3
add 6
'''


#!/bin/bash

import os
import sys

def maximumProgramValue(n):
	x = 0

	for i in xrange(0, n):
		instruction = str(raw_input())
		if instruction[:3] == "add":
			if int(instruction[4:]) > 0:
				x += int(instruction[4:])

		if instruction[:3] == "set":
			if int(instruction[4:]) > x:
				x = int(instruction[4:])


	print x


if __name__ == '__main__':
	n = int(raw_input())
	maximumProgramValue(n)