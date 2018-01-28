'''input
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba
'''

#!/bin/python

# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import sys

def designerPdfViewer(h, word):
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	maxH = 0
	for letter in word:
		if h[alphabet.index(letter)] > maxH:
			maxH = h[alphabet.index(letter)]


	return str(len(word) * maxH)

if __name__ == "__main__":
	h = map(int, raw_input().strip().split(' '))
	word = raw_input().strip()
	result = designerPdfViewer(h, word)
	print result