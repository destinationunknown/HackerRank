'''input
1
#####R##
##P#####
########
########
########
#####B##
#K####k#
########
'''

#!/bin/python

import sys 

def waysToGiveACheck(board):
	checkCount = 0

	# Find the position of the valid pawn:
	for k in [i for i, x in enumerate(board[1]) if x == 'P']:
		if board[0][k] == "#":
			# Move the pawn
			board[0][k] = "*"
			board[1][k] = '#'

			pawnPos = [0, k]

	# Find the position of the King
	for i in xrange(7):
		if 'k' in board[i]:
			kingPos = [board[i].index('k'), i]

	#
	# Check for Knight
	#

	# Check 2 units up, 1 unit to the left
	if kingPos[0] >= 1 and kingPos[1] >= 2:
		if board[kingPos[1] - 2][kingPos[0] - 1] == 'N' or board[kingPos[1] - 2][kingPos[0] - 1] == '*':
			checkCount += 1

	# Check 2 units up, 1 unit to the right
	if kingPos[0] <= 6 and kingPos[1] >= 2:
		if board[kingPos[1] - 2][kingPos[0] + 1] == 'N' or board[kingPos[1] - 2][kingPos[0] + 1] == '*':
			checkCount += 1

	# Check 2 units down, 1 unit to the left
	if kingPos[0] >= 1 and kingPos[1] <= 5:
		if board[kingPos[1] + 2][kingPos[0] - 1] == 'N' or board[kingPos[1] + 2][kingPos[0] - 1] == '*':
			checkCount += 1

	# Check 2 units down, 1 unit to the right
	if kingPos[0] <= 6 and kingPos[1] <= 5:
		if board[kingPos[1] + 2][kingPos[0] + 1] == 'N' or board[kingPos[1] + 2][kingPos[0] + 1] == '*':
			checkCount += 1

	# Check 1 unit up, 2 units to the left
	if kingPos[0] >= 2 and kingPos[1] >= 1:
		if board[kingPos[1] - 1][kingPos[0] - 2] == 'N' or board[kingPos[1] - 1][kingPos[0] - 2] == '*':
			checkCount += 1

	# Check 1 unit up, 2 units to the right
	if kingPos[0] <= 5 and kingPos[1] >= 1:
		if board[kingPos[1] - 1][kingPos[0] + 2] == 'N' or board[kingPos[1] - 1][kingPos[0] + 2] == '*':
			checkCount += 1

	# Check 1 unit down, 2 units to the left
	if kingPos[0] >= 1 and kingPos[1] <= 6:
		if board[kingPos[1] + 1][kingPos[0] - 2] == 'N' or board[kingPos[1] + 1][kingPos[0] - 2] == '*':
			checkCount += 1

	# Check 1 unit down, 2 units to the right
	if kingPos[0] <= 5 and kingPos[1] <= 6:
		if board[kingPos[1] - 1][kingPos[0] + 2] == 'N' or board[kingPos[1] + 1][kingPos[0] + 2] == '*':
			checkCount += 1

	#
	# Check for Rook
	#

	# Check left
	
	for i in xrange(kingPos[0] - 1, -1 , -1):
		if board[kingPos[1]][i] != '#':
			if board[kingPos[1]][i] == 'R':
				checkCount += 1
			if board[kingPos[1]][i] == '*':
				checkCount += 2 	# Add 1 for transformed into Rook, 1 for transformed into Queen
			else:
				break

	# Check right
	for i in xrange(kingPos[0] + 1 , 8):
		if board[kingPos[1]][i] != '#':
			if board[kingPos[1]][i] == 'R':
				checkCount += 1
			if board[kingPos[1]][i] == '*':
				checkCount += 2 	# Add 1 for transformed into Rook, 1 for transformed into Queen
			else:
				break

	# Check up
	for i in xrange(kingPos[1] - 1, -1, -1):
		if board[i][kingPos[0]] != '#':
			if board[i][kingPos[0]]  == 'R':
				checkCount += 1
			if board[i][kingPos[0]]  == '*':
				checkCount += 2 	# Add 1 for transformed into Rook, 1 for transformed into Queen
			else:
				break

	# Check down
	for i in xrange(kingPos[1] + 1, 8):
		if board[i][kingPos[0]] != '#':
			if board[i][kingPos[0]]  == 'R':
				checkCount += 1
			if board[i][kingPos[0]]  == '*':
				checkCount += 2 	# Add 1 for transformed into Rook, 1 for transformed into Queen
			else:
				break

	#
	# Check for Bishop
	#

	# Up and left
	for i in xrange(kingPos[0] - 1, -1 , -1):
		print "i; " + str(i)
		print str(kingPos[1]-i) + "," + str(i)
		if board[kingPos[1]-i][i] != '#':
			if board[kingPos[1]][i] == 'B':
				checkCount += 1
			if board[kingPos[1]][i] == '*':
				checkCount += 2 	# Add 1 for transformed into Rook, 1 for transformed into Queen
			else:
				break

	print "Pawn position: " + str(pawnPos)
	print "King position " + str(kingPos)

	return checkCount


if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        board = []
        for board_i in xrange(8):
            board_temp = map(str, raw_input().strip())
            board.append(board_temp)
        result = waysToGiveACheck(board)
        print result