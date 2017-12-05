from visualization.message import message
from utility.input_string import input_string
from visualization.print_protein import print_protein
from utility.update_grid import update_grid
from utility.fold import fold
from utility.score import score
from algorithms.hillclimber import hillclimber
from algorithms.algo_brute_force import brute_force
from plotting.plots import plothillclimber

import csv

# Import all the global variables.
import global_vars
global_vars.init()


def main():

    message("This is a protein-fold-optimizer by Team50")

    # Get the user's choice of protein.
    input_string()

    message("Protein received")

    # Print starting configuration of the protein
    print_protein()

    algorithm = 0

    while not algorithm == 1 and not algorithm == 2 and not algorithm == 3:
        algorithm = int(input("Type 1 for Brute Force \n Type 2 for Hill Climber \n Type 3 for Hill Climber with Simulated Annealing \n What algorithm do you want to use? "))

    message("Protein initiated, starting algorithm.")

    if algorithm == 1:
        brute_force()

    if algorithm == 2:
        hillclimber()

    if algorithm == 3:
        print("This algorithm hasn't been implemented yet!")
    
    print_protein()
    print("Score: " + str(global_vars.winning_score), end = '\n\n')
    
    if algorithm == 2:
        plothillclimber()



if __name__ == '__main__':
	main()
