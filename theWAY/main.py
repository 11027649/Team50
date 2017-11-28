from message import message
from input_string import input_string
from print_protein import print_protein, debug_print_protein
from update_grid import update_grid
from fold import fold
from score import score
from hillclimber import hillclimber

from plotdata import plotdata
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
    debug_print_protein()

    message("Protein initiated, starting algorithm.")

    """>>>>>> UNCOMMENT THE ALGORITHM YOU WANT TO USE BELOW <<<<<<"""

    # algo_brute_force()

    # Print the best solution.


    hillclimber()
    print_protein()

    print("Score: " + str(global_vars.winning_score), end = '\n\n')

if __name__ == '__main__':
	main()
