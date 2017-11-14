def score(grid, protein):
	""" Takes a grid with the folded protein in it. Returns a stability score. """

	score = 0
	columns = len(grid)
	rows = len(grid[1])

	# iterate over columns
	for y in range(rows):

		# iterate over rows
		for x in range(columns):

	        # makes sure it is a letter
			if not grid[x][y] == ' ':

				if grid[x][y].letter == 'H':
					if not x == 0 and not grid[x - 1][y] == ' ':
						if grid[x - 1][y].letter == 'H':
							score -= 0.5
					if not x == columns - 1 and not grid[x + 1][y] == ' ':
						if grid[x + 1][y].letter == 'H':
							score -= 0.5
					if not y == rows - 1 and not grid[x][y + 1] == ' ':
						if grid[x][y + 1].letter == 'H' :
							score -= 0.5
					if not y == 0 and not grid[x][y - 1] == ' ':
						if grid[x][y - 1].letter == 'H':
							score -= 0.5

	for i in range(len(protein) - 1):
		if protein[i].letter == 'H':
			if protein[i + 1].letter == 'H':
				score += 1
	return score
