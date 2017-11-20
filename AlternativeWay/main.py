from print_mess import print_mess
from input_string import input_string
from print_protein import print_protein
from fold import fold
from score import score

import global_vars
global_vars.init()


print_mess("This is a protein-fold-optimizer by Team50")

input_string()

print_mess("Protein received")

print_protein()

print_mess("Protein initiated")

print_mess("Folding summary:")

fold(3, "L")
fold(8, "L")
fold(9, "L")
fold(1, "L")
fold(11, "L")

print_mess("Printing protein")

print_protein()

print_mess("Checking score")

print("score: " + str(score()), end='\n\n')
