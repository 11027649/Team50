from print_mess import print_mess
from input_string import input_string
from print_protein import print_protein
from fold import fold
from score import score

from algo_brute_force import algo_brute_force

import global_vars
global_vars.init()


print_mess("This is a protein-fold-optimizer by Team50")

input_string()

print_mess("Protein received")

print_protein()

print_mess("Protein initiated, starting algorithm.")

print_mess("Folding summary:")

algo_brute_force()

# print_mess("Printing protein")
#
# print_protein()
