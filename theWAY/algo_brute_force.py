# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: algo_brute_force, recursive_function, fold_all_right.
# 
# Fold all right makes a spiral of the protein. This was to try if the fold and
# score function worked right.
#
# The algo_brute_force tries every foldation of the protein.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import amino
from score import score
from fold import fold
from print_protein import print_protein
import time
import copy

import global_vars
global_vars.init()


<<<<<<< HEAD
=======
def algo_brute_force():
    """ This algorithm tries every possibility of foldation of the protein. 
        Therefore it uses the global coordinates. It stores the amount of "best"
        solutions in a global variable called amount.
        In a unlogical, unefficient way for now.. 
        It's not working yet to save the winning coordinates."""
>>>>>>> 65b353e3e7e281793084df1348973e4044906ecd

def algo_brute_force():

    def recursive_function(depth):

        current_score = score()

        if current_score < global_vars.winning_score:

            global_vars.winning_score = current_score
            global_vars.winning_grid = copy.deepcopy(global_vars.grid)
            global_vars.amount += 1
            # print(winning_coordinates)
            print("\n\nBest so far, stability of " + str(global_vars.winning_score) + ":\n")
            print_protein()


        if (depth < 1):
            return

        fold(depth, "L")
        recursive_function(depth - 1)
        fold(depth, "R")
        recursive_function(depth - 1)
        fold(depth, "R")
        recursive_function(depth - 1)
        fold(depth, "L")


    length = len(global_vars.protein_string)
    depth = length - 2
    steps = pow(3, len(global_vars.protein_string) - 2)
    sps = 3000

    if input("This brute force algorithm will take " + str(steps) + " steps. \nThat equals approx. "+ str(int(steps / (sps * 60))) +"m "+ str(round(60*((steps / (sps * 60)) % 1), 2)) +"s.\n U sure? (y/n) ").upper() == "Y":
        print()

        start = time.time()
        # fold_all_right()
        recursive_function(depth)

        end = time.time()

        print("Best solution found with a stability of " + str(global_vars.winning_score) + " in: " + str(int((end - start) / 60)) + "m " + str(round(((end - start) % 60), 2)) + "s.")
        print()

        # print(winning_coordinates)
        global_vars.grid = global_vars.winning_grid

    else:
        print("\nStopping program\n")
        exit(1)


def fold_all_right():
    for i in range(1, len(global_vars.protein_string) - 1):
        fold(i, "R")
