import matplotlib.pyplot as plt
import numpy as np
import csv

# import global vars to use te coordinates in plot protein
import global_vars
global_vars.init()

def plot_hillclimber():
	filepath = global_vars.filepath
	data = np.genfromtxt(filepath, delimiter=',', names=['x', 'y'])
    
	fig = plt.figure()

	ax = fig.add_subplot(111)

	ax.set_title('Hill Climber')
	ax.set_xlabel('Iteration')
	ax.set_ylabel('Stability')

	ax.plot(data['x'], data['y'], color='r', label='stability')

	plt.show()

def plot_simulated_annealing():
	filepath = global_vars.filepath
	data = np.genfromtxt(filepath, delimiter=',', names=['x', 'y'])
	fig = plt.figure()

	ax = fig.add_subplot(111)

	ax.set_title('Simulated Annealing')
	ax.set_xlabel('Iteration')
	ax.set_ylabel('Stability')

	ax.plot(data['x'], data['y'], color = 'r', label = 'stability')
	
	plt.show()


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as mlines

def plot_best_protein():

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	plt.rcParams["font.size"] = 10

	coor = global_vars.protein.winning_coordinates
	protein = global_vars.protein.protein_string 

	X = []
	Y = []
	Z = []

	# add coordinates to X and Y array
	for i in range(len(protein)):
		X.append(coor[i][0])
		Y.append(coor[i][1])
		Z.append(coor[i][2])

	# scatter points, plot the aminos in the right colors
	for i in range(len(protein)):
		if protein[i] == 'H':
			ax.scatter(X[i],Y[i], Z[i], marker = 'o', s = 200, color="blue")
		elif protein[i] == 'C':
			ax.scatter(X[i], Y[i], Z[i], marker = 'o', s = 200, color = "yellow")
		else:
			ax.scatter(X[i],Y[i], Z[i], marker='o', s = 200, color="red")

	ax.set_title('Protein with best score')

	# plot solid lines for bonds
	ax.plot(X,Y,Z, linestyle='solid', color="black")

	X = np.array(X)
	Y = np.array(Y)
	Z = np.array(Z)


	# Create cubic bounding box to simulate equal aspect ratio
	max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
	Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
	Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
	Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())

	# Comment or uncomment following both lines to test the fake bounding box:
	for xb, yb, zb in zip(Xb, Yb, Zb):
	   ax.plot([xb], [yb], [zb], 'w')


	plt.axis('off')
	# plt.axis('equal')

	fig.text(.1,.1, "Stability: " + str(global_vars.protein.winning_score))
	
	plt.show()
