'''input
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
'''

#!/bin/python

import sys

def matrixRotation(matrix, r):
	lcm = 0
	layers = min(len(matrix), len(matrix[0]))/2

	for i in xrange(0, layers):
		layer = []


		# Get left and right
		left = []
		right = []
		top = []
		bottom = []
		for k in xrange(i, len(matrix) - i):
			left.append(matrix[k][i])
			right.append(matrix[k][len(matrix[k])-1-i])
		
		# Get top and bottom
		for k in xrange(i, len(matrix[0]) - i):
			top.append(matrix[i][k])
			bottom.append(matrix[len(matrix)-1-i][k])

		# Remove the first and last elements of top and bottom
		del top[0]
		del top[len(top)-1]
		del bottom[0]
		del bottom[len(bottom)-1]

		# Reverse right and top
		right = right[::-1]
		top = top[::-1]

		layer = left[:]
		layer.extend(bottom)
		layer.extend(right)
		layer.extend(top)

	

		if (r+i) >= len(layer):
			rot = (r) % len(layer)
		else:
			rot = r

		# Rotate the layer
		newlayer = layer[-rot:] + layer[:-rot] 

		rotated = matrix[:]

		# Get the new left, bottom, right and top arrays from the rotated layer

		x = len(matrix[0])
		y = len(matrix)

		newleft = newlayer[0:len(matrix)-2*i]
		newbottom = newlayer[len(matrix)-2*i-1: len(matrix)-4*i + len(matrix[0])-1]
		
		newright = newlayer[len(matrix)-4*i + len(matrix[0])-2: len(matrix)-6*i + len(matrix[0]) + len(matrix)-2]
		newright = newright[::-1]
		
		newtop = newlayer[-len(matrix[0]) +1+2*i:]
		newtop.append(newlayer[0])
		newtop = newtop[::-1]


		for index, k in enumerate(xrange(i, len(matrix) - i)):
 			rotated[k][i] = newleft[index]
 			rotated[k][x-i-1] = newright[index]

 		for index, k in enumerate(xrange(i, len(matrix[0]) -i)):
 			rotated[i][k] = newtop[index]
 			rotated[y-i-1][k] = newbottom[index]


 	for row in rotated:
 		for elem in row:
 			print elem,
 		print 

if __name__ == "__main__":
	m, n, r = raw_input().strip().split(' ')
	m, n , r = [int(m), int(n), int(r)]
	matrix = []
	for matrix_i in xrange(m):
		matrix_temp = map(int, raw_input().strip().split(' '))
		matrix.append(matrix_temp)
	matrixRotation(matrix, r)


