import matplotlib.pyplot as plt
import numpy as np
import csv

def plotdata():
    data = np.genfromtxt('hillclimber.csv', delimiter=',', names=['x', 'y'])

    fig = plt.figure()

    graph = fig.add_subplot(111)

    graph.set_title("Hill Climber")
    graph.set_xlabel('Iteration')
    graph.set_ylabel('Stability')

    graph.plot(data['x'], data['y'], color='r', label='stability')

    plt.show()
