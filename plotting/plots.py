import matplotlib.pyplot as plt
import numpy as np
import csv

# import global vars to use te coordinates in plot protein
import global_vars
global_vars.init()

def plothillclimber():
    data = np.genfromtxt('hillclimber.csv', delimiter=',', names=['x', 'y'])

    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.set_title('Hill Climber')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Stability')

    ax.plot(data['x'], data['y'], color='r', label='stability')

    plt.show()

from mpl_toolkits.mplot3d import Axes3D

def plot_best_protein():

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	coor = global_vars.winning_coordinates
	protein = global_vars.protein_string 

	X = []
	Y = []

	# add coordinates to X and Y array
	for i in range(len(protein)):
		X.append(coor[i][0])
		Y.append(coor[i][1])


	for i in range(len(protein)):
		if protein[i] == 'H':
			ax.scatter(X[i],Y[i],0, marker = 'o', s = 375, color="blue")
		else:
			ax.scatter(X[i],Y[i],0, marker='o', s = 375, color="red")

	ax.set_title('Protein with best score')

	ax.plot(X,Y,0, linestyle='-', color="black")

	plt.axis('equal')
	plt.axis('off')
	plt.show()
