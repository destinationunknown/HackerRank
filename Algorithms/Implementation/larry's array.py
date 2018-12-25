'''input
3
3
3 1 2
4
1 3 4 2
5
1 2 3 5 4
'''

#!/bin/python

import sys

def larrysArray(A):
	isSorted = False

	while not isSorted:
		isSorted = True
		for index,elem in enumerate(A):
			original = A
			B = A[::]

			if index != 0 and index != len(A)-1:

				if elem < A[index-1]:
					isSorted = False

				if A[index-1] > elem and A[index+1] > elem and A[index-1] > A[index+1]:
					B[index-1] = elem
					B[index] = A[index+1]
					B[index+1] = A[index-1]

				if A[index-1] < elem and elem > A[index+1]:
					B[index-1] = A[index+1]
			 		B[index] = A[index-1]
					B[index+1] = A[index]

					A = B[::]

			if index != 0:
				if elem < A[index-1]:
					isSorted = False

		if not isSorted and A == original:
			return "YES"

	return "NO"


if __name__ == "__main__":
	t = int(raw_input().strip())
	for a0 in xrange(t):
		n = int(raw_input().strip())
		A = map(int, raw_input().strip().split(' '))
		result = larrysArray(A)
		print result