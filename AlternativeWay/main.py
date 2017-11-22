from message import message
from input_string import input_string
from print_protein import fancy_print
from print_protein import print_protein
from fold import fold
from score import score

from algo_brute_force import algo_brute_force

import global_vars
global_vars.init()

message("This is a protein-fold-optimizer by Team50")

input_string()

message("Protein received")


print_protein()

message("Protein initiated, starting algorithm.")

message("Folding summary:")

algo_brute_force()

message("We found " + str(global_vars.amount) + " best solutions.")
