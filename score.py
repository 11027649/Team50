def score(grid):
	""" Takes a grid with the folded protein in it. Returns a stability score. """

	rows = len(grid)
	columns = len(grid[0])

	# iterate over columns
	for i in range(columns):

		# iterate over rows
		for j in range(rows):

			# check if H, and if yes, check stability
			if grid[i][j] == 'H'

				if not j == 0:
					# check if above is an H
					if (grid[i][j + 1] == 'H'): #(and if not bonded)
						score = score - 0.5

				if not j == rows:
					# check if beneath is an H
					if (grid[i][j - 1] == 'H'): #(and if not bonded)
						score = score - 0.5

				if not i == columns:
					# check if right is an H
					if grid[i + 1][j] == 'H':
						score = score - 0.5

				if not i == 0:
					# check if left is an H
					if grid[i - 1][j] == 'H':
						score = score - 0.5

	return score
