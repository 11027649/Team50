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

    message("Protein initiated, starting algorithm.")

    """>>>>>> UNCOMMENT THE ALGORITHM YOU WANT TO USE BELOW <<<<<<"""
    # brute_force()

    # hillclimber()
    
    print_protein()
    print("Score: " + str(global_vars.winning_score), end = '\n\n')
    
    """>>>>> UNCOMMENT THIS IF YOU WANT TO RUN A HILLCLIMBER ÁND PLOT THE DATA <<<<<<"""
    # plothillclimber()



if __name__ == '__main__':
	main()
