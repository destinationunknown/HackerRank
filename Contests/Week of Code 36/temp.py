def waysToGiveACheckWrong(board):
	xcheckCount = 0

	# Find the valid pawn:
	for k in [i for i, x in enumerate(board[1]) if x == 'P']:
		if board[0][k] == "#":
			pos = k

	# Case 1: Transformed into Knight

	if pos >= 1:
		# Check for check on 2 units down, 1 unit to the left
		if board[2][pos-1] == 'k':
			xcheckCount += 1

	if pos <= 6:
		# Check 2 units down, 1 unit to the right
		if board[2][pos+1] == 'k':
			xcheckCount += 1

	if pos >= 2:
		# Check 1 unit down, 2 units to the left
		if board[1][pos-2] == 'k':
			xcheckCount += 1

	if pos <= 5:
		# Check 1 unit down, 2 units to the right
		if board[1][pos+2] == 'k':
			xcheckCount += 1

	# Case 2: Transformed into Rook

	for i in xrange(pos):
		# Check left
		if board[0][pos-i-1] is not '#':
			if board[0][pos-i-1] == 'k':
				xcheckCount += 1
			else:
				break

	for i in xrange(7-pos):
		# Check right
		if board[0][pos+i-1] is not '#':
			if board[0][pos+i-1] == 'k':
				xcheckCount += 1
			else:
				break

	for i in xrange(6):
		# Check vertically
		if board[i+1][pos] is not '#':
			if board[i+1][pos] == 'k':
				xcheckCount += 1
			else:
				break


	# Case 3: Transformed into Bishop

	if pos >= 1:
		# Check diagonally left
		for i in xrange(pos):
			#print 'i: ' + str(i)
			#print str(1+i) + ", " + str(pos-i - 1)
			#print "piece: " + str(board[1+i][pos-i -1])
			if board[1+i][pos-i -1] is not '#':
				if board[1+i][pos-i-1] == 'k':
					xcheckCount += 1
				else:
					break

	if pos <= 6:
		# Check diagonally right 
		for i in xrange(7 - pos):
			if board[1+i][pos+i -1] is not '#':
				if board[1+i][pos+i-1] == 'k':
					xcheckCount += 1
				else:
					break


	# Case 4: Transformed into a Queen
	# Check for Bishop and Rook

	for i in xrange(7-pos):
		# Check right
		if board[0][pos+i-1] is not '#':
			if board[0][pos+i-1] == 'k':
				xcheckCount += 1
			else:
				break

	for i in xrange(6):
		# Check vertically
		if board[i+1][pos] is not '#':
			if board[i+1][pos] == 'k':
				xcheckCount += 1
			else:
				break


	if pos >= 1:
		# Check diagonally left
		for i in xrange(pos):
			#print 'i: ' + str(i)
			#print str(1+i) + ", " + str(pos-i - 1)
			#print "piece: " + str(board[1+i][pos-i -1])
			if board[1+i][pos-i -1] is not '#':
				if board[1+i][pos-i-1] == 'k':
					xcheckCount += 1
				else:
					break

	if pos <= 6:
		# Check diagonally right 
		for i in xrange(7 - pos):
			if board[1+i][pos+i -1] is not '#':
				if board[1+i][pos+i-1] == 'k':
					xcheckCount += 1
				else:
					break

	return xcheckCount