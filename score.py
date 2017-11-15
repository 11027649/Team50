# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# contains score
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def score(grid, protein):
	""" Takes a grid with the folded protein in it. Returns a stability score,
		that is calculated by distracting 0.5 everytime H amino acids are next
		to each other on the grid.Also takes the protein, and adds the 'normal' 
		bounds to the score. """

	# set up variables
	score = 0
	columns = len(grid)
	rows = len(grid[1])

	# iterate over columns
	for y in range(rows):

		# iterate over rows
		for x in range(columns):

	        # makes sure it is a letter
			if not grid[x][y] == ' ':

				# the stability can only come from H's
				if grid[x][y].letter == 'H':

					# if not in the first column and the grid spot on the left
					# is not empty
					if not x == 0 and not grid[x - 1][y] == ' ':
						
						# check if left is H
						if grid[x - 1][y].letter == 'H':
							
							# adjust score
							score -= 0.5

					# same for right, above and under
					if not x == columns - 1 and not grid[x + 1][y] == ' ':
						if grid[x + 1][y].letter == 'H':
							score -= 0.5

					if not y == rows - 1 and not grid[x][y + 1] == ' ':
						if grid[x][y + 1].letter == 'H' :
							score -= 0.5

					if not y == 0 and not grid[x][y - 1] == ' ':
						if grid[x][y - 1].letter == 'H':
							score -= 0.5

	# iterate over the protein and add 1 for each normal bond (these don't count
	# for stability)
	for i in range(len(protein) - 1):
		if protein[i].letter == 'H':
			if protein[i + 1].letter == 'H':
				score += 1
	
	return score
