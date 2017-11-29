import matplotlib.pyplot as plt
import numpy as np
import csv

def plothillclimber():
    data = np.genfromtxt('data/hillclimber.csv', delimiter=',', names=['x', 'y'])

    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.set_title('Hill Climber')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Stability')

    ax.plot(data['x'], data['y'], color='r', label='stability')

    plt.show()

from mpl_toolkits.mplot3d import axes3d

def plot_best_protein():
	# data = np.genfromtxt('protein.csv', delimiter=',', names=['x','y','z'])

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	X,Y,Z = [1,2,3,4,5,6,7,8,9,10],[5,6,8,13,4,1,2,4,8],[2,3,3,3,5,7,9,11,9,10]

	ax.set_title('Protein with best score')
	# ax.scatter(data['x'], data['y'], data['z'], c='r', marker='o')
	ax.plot_wireframe(X,Y,Z)
	# ax.scatter(X,Y,Z, c='r', marker='o')


	plt.show()