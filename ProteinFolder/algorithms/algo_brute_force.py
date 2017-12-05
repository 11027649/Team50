# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: brute_force, foldings_recursive.
#
# The algo_brute_force tries every foldation of the protein (multiple times for
# for now ;-P).
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import amino
from utility.score import score
from utility.fold import fold
from visualization.print_protein import print_protein

import time
import copy

import global_vars
global_vars.init()

def brute_force():
    """ This algorithm tries every possibility of foldation of the protein.
        Therefore it uses the global coordinates. It stores the amount of "best"
        solutions in a global variable called amount.
        In a unlogical, unefficient way for now..
        It's not working yet to save the winning coordinates."""

    print("Brute forcing...")

    length = len(global_vars.protein_string)
    depth = length - 2
    steps = pow(3, len(global_vars.protein_string) - 2)
    sps = 3000
    # initialize winning grid and coordinates to make sure they are not empty
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)

    if input("This brute force algorithm will take " + str(steps) + " steps. \nThat equals approx. "+ str(int(steps / (sps * 60))) +"m "+ str(round(60*((steps / (sps * 60)) % 1), 2)) +"s.\n Are you sure you want to start? (y/n) ").upper() == "Y":
        print()

        start = time.time()
        # fold_all_right()
        foldings_recursive(depth)

        end = time.time()

        print("Best solution found with a stability of " + str(global_vars.winning_score) + " in: " + str(int((end - start) / 60)) + "m " + str(round(((end - start) % 60), 2)) + "s.")
        print()

        # save winning coordinates and grid
        global_vars.grid = copy.deepcopy(global_vars.winning_grid)
        global_vars.coordinates = copy.deepcopy(global_vars.winning_coordinates)


    else:
        print("\nStopping program\n")
        exit(1)

def foldings_recursive(depth):

    current_score = score()

    if current_score < global_vars.winning_score:

        global_vars.winning_score = current_score
        global_vars.winning_grid = copy.deepcopy(global_vars.grid)
        global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)
        global_vars.amount += 1
        # print(winning_coordinates)
        print("\n\nBest so far, stability of " + str(global_vars.winning_score) + ":\n")
        print_protein()


    if (depth < 1):
        return

    fold(depth, "L")
    foldings_recursive(depth - 1)
    fold(depth, "R")
    foldings_recursive(depth - 1)
    fold(depth, "R")
    foldings_recursive(depth - 1)
    fold(depth, "L")

def brute_force_tyfen():
    print("hoi")
