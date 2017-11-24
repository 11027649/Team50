import matplotlib.pyplot as plt
import numpy as np
import csv

def plotdata():
    data = np.genfromtxt('data.csv', delimiter=',', names=['x', 'y'])

    fig = plt.figure()

    ax1 = fig.add_subplot(111)



    ax1.set_title("Hill Climber")
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Stability')

    ax1.plot(data['x'], data['y'], color='r', label='stability')

    plt.show()
