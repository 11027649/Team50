import matplotlib.pyplot as plt
import numpy as np
import csv

# import global vars to use te coordinates in plot protein
import global_vars
global_vars.init()

def plot_hillclimber():
    data = np.genfromtxt('hillclimber.csv', delimiter=',', names=['x', 'y'])
    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.set_title('Hill Climber')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Stability')

    ax.plot(data['x'], data['y'], color='r', label='stability')

    plt.show()

def plot_simulated_annealing():
	data = np.genfromtxt('simulated_annealing.csv', delimiter=',', names=['x', 'y'])
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

	coor = global_vars.winning_coordinates
	protein = global_vars.protein_string 

	X = []
	Y = []

	# add coordinates to X and Y array
	for i in range(len(protein)):
		X.append(coor[i][0])
		Y.append(coor[i][1])

	# scatter points, plot the aminos in the right colors
	for i in range(len(protein)):
		if protein[i] == 'H':
			ax.scatter(X[i],Y[i],0, marker = 'o', s = 300, color="blue", zorder = 2)
		elif protein[i] == 'C':
			ax.scatter(X[i], Y[i], marker = 'o', s = 300, color = "yellow", zorder = 3)
		else:
			ax.scatter(X[i],Y[i],0, marker='o', s = 300, color="red", zorder = 4)

	ax.set_title('Protein with best score')

	# plot solid lines for bonds
	ax.plot(X,Y,0, linestyle='solid', color="black", zorder = 1)

	plt.axis('equal')
	plt.axis('off')
	
	plt.show()
