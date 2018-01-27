'''input
44
84
94
21
0
18
100
18
62
30
61
53
0
43
2
29
53
61
40
14
4
29
98
37
23
46
9
79
62
20
38
51
99
59
47
4
86
61
68
17
45
6
1
95
95
'''

#!/bin/python

import sys

def solve(grades):
	# r
	grades_solved = []
	for grade in grades:
		if int(grade) >= 38:
			if int(grade[1]) > 5:
				if (10 - int(grade[1])) < 3:
					grades_solved.append(str(int(grade[0]) + 1)  + "0")
				else:
					grades_solved.append(grade)
			if int(grade[1]) <= 5:
				if (5 - int(grade[1])) < 3:
					grades_solved.append(grade[0] + "5")
				else:
					grades_solved.append(grade)
		else:
			grades_solved.append(grade)
	return grades_solved

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
		grades_t = raw_input().strip()
		grades.append(grades_t)

result = solve(grades)
print "\n".join(map(str, result))