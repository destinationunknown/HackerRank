'''input
3
hydrochloric
rainbowic
idontevenknow
'''

#!/bin/python

def acidNaming(acid_name):
	
	if acid_name[-2:] == "ic":
		if acid_name[:5] == "hydro":
			return "non-metal acid"
		else:
			return "polyatomic acid"
	else: 
		return "not an acid"

if __name__ == "__main__":
	n = int(raw_input().strip())
	for a0 in xrange(n):
		acid_name = raw_input().strip()
		result  = acidNaming(acid_name)
		print result
