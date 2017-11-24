from message import message
from input_string import input_string
from print_protein import fancy_print_protein
from print_protein import print_protein
from update_grid import update_grid
from fold import fold
from score import score
from hillclimber import hillclimber
from algo_brute_force import algo_brute_force

# Import all the global variables.
import global_vars
global_vars.init()

message("This is a protein-fold-optimizer by Team50")

# Get the user's choice of protein.
input_string()

message("Protein received")

# Print starting configuration of the protein
print_protein()

message("Protein initiated, starting algorithm.")

message("Folding summary:")

""">>>>>> UNCOMMENT THE ALGORITHM YOU WANT TO USE BELOW <<<<<<"""

algo_brute_force()
# hillclimber()

# Print the best solution.
print_protein()
