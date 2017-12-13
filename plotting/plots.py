import matplotlib.pyplot as plt
import numpy as np
import csv

from protein_class import Amino

def plot_data(run_info):
	filepath = run_info.filepath
	data = np.genfromtxt(filepath, delimiter=',', names=['x', 'y'])
	fig = plt.figure()

	ax = fig.add_subplot(111)

	if (run_info.dimension == 0):
		dimension = '2D'
	else:
		dimension = '3D'
	
	ax.set_title(run_info.algorithm + ' for: ' + run_info.protein_name + ' in: ' + dimension)

	ax.set_xlabel('Iteration')
	ax.set_ylabel('Stability')

	ax.plot(data['x'], data['y'], color = 'r', label = 'stability')

	plt.show()


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as mlines

def plot_best_protein(protein, run_info):

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	plt.rcParams["font.size"] = 10

	coor = protein.winning_coordinates

	X = []
	Y = []
	Z = []

	# add coordinates to X and Y array
	for i in range(protein.protein_length):
		X.append(coor[i][0])
		Y.append(coor[i][1])
		Z.append(coor[i][2])

	# scatter points, plot the aminos in the right colors
	for i in range(protein.protein_length):
		if protein.protein_string[i] == 'H':
			ax.scatter(X[i],Y[i], Z[i], marker = 'o', s = 200, color="blue")
		elif protein.protein_string[i] == 'C':
			ax.scatter(X[i], Y[i], Z[i], marker = 'o', s = 200, color = "yellow")
		else:
			ax.scatter(X[i],Y[i], Z[i], marker='o', s = 200, color="red")

	ax.set_title('Best score for: ' + run_info.protein_name)

	ax.set_xlabel('X axis')
	ax.set_ylabel('Y axis')
	ax.set_zlabel('Z axis')

	# plot solid lines for bonds
	ax.plot(X,Y,Z, linestyle='solid', color="black")

	# plot dashed lines for interactions
	grid = protein.winning_grid
	coordinates = protein.winning_coordinates[:]

	cystein_appearance = False

	# for all aminos in the protein
	for i in range(protein.protein_length):

	# the coordinates are stored in an array. i is the amino acid that you're
	# looking for, [0] or [1] are x and y
		x = coordinates[i][0]
		y = coordinates[i][1]
		z = coordinates[i][2]

		# save the current id of the amino acid
		cur_id = grid[x][y][z].num_id

		if (grid[x][y][z].letter == "C"):
			cystein_appearance = True

		# if it's an H, do something with the score
		# check only under and to the right to not count interactions double
		if grid[x][y][z].letter == "H" or grid[x][y][z].letter == "C":

			if type(grid[x + 1][y][z]) == Amino \
				and grid[x + 1][y][z].letter == grid[x][y][z].letter \
				and abs(cur_id - grid[x + 1][y][z].num_id) > 1:

				to_id = grid[x + 1][y][z].num_id

				XX = [X[cur_id], X[to_id]]
				YY = [Y[cur_id], Y[to_id]]
				ZZ = [Z[cur_id], Z[to_id]]
				ax.plot(XX, YY, ZZ, linestyle='dotted', color="black")


			# same for under
			if type(grid[x][y + 1][z]) == Amino \
			and grid[x][y + 1][z].letter == grid[x][y][z].letter \
			and abs(cur_id - grid[x][y + 1][z].num_id) > 1:

				to_id = grid[x][y + 1][z].num_id

				XX = [X[cur_id], X[to_id]]
				YY = [Y[cur_id], Y[to_id]]
				ZZ = [Z[cur_id], Z[to_id]]
				ax.plot(XX, YY, ZZ, linestyle='dotted', color="black")

			# same for "beneath" (at z axis)
			if type(grid[x][y][z + 1]) == Amino \
			and grid[x][y][z + 1].letter == grid[x][y][z].letter \
			and abs(cur_id - grid[x][y][z + 1].num_id) > 1:

				to_id = grid[x][y][z + 1].num_id

				XX = [X[cur_id], X[to_id]]
				YY = [Y[cur_id], Y[to_id]]
				ZZ = [Z[cur_id], Z[to_id]]
				ax.plot(XX, YY, ZZ, linestyle='dotted', color="black")

	X = np.array(X)
	Y = np.array(Y)
	Z = np.array(Z)

	# create cubic bounding box to simulate equal aspect ratio
	# source:
	max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
	Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
	Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
	Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())

	# comment or uncomment following both lines to test the fake bounding box:
	for xb, yb, zb in zip(Xb, Yb, Zb):
	   ax.plot([xb], [yb], [zb], 'w')

	# set legend
	polar = mlines.Line2D([], [], color='red', marker='o', markersize=15, label='Polar')
	apolar = mlines.Line2D([], [], color='blue', marker='o', markersize=15, label='Apolar')

	if cystein_appearance == True:
		cystein = mlines.Line2D([], [], color='yellow', marker='o', markersize=15, label='Cystein')
		legend = [cystein, polar, apolar]
	elif cystein_appearance == False:
		legend = [polar, apolar]
	
	plt.legend(handles=legend)

	fig.text(.1,.1, "Stability: " + str(protein.winning_score))

	plt.show()
