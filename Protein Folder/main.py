from visualization.message import message
from utility.input_string import input_string
from visualization.print_protein import print_protein
from utility.update_grid import update_grid
from utility.fold import fold
from utility.score import score
from algorithms.hillclimber import hillclimber
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

    message("Protein initiated, starting algorithm.")

    """>>>>>> UNCOMMENT THE ALGORITHM YOU WANT TO USE BELOW <<<<<<"""

    # with open('optimization.csv', 'a', newline='') as csvfile:
    #     writer = csv.writer(csvfile)

    #     for i in range(2, 14):
    #         print(i)
    #         for j in range(25):
    #             print("  ", end='')
    #             print(j)
    #             hillclimber(i)
    #             writer.writerow([i] + [global_vars.winning_score])

    hillclimber()
    print_protein()
    print("Score: " + str(global_vars.winning_score), end = '\n\n')
    plothillclimber()





if __name__ == '__main__':
	main()
