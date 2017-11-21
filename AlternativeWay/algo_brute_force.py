from global_vars import amino
from score import score
from fold import fold
from print_protein import print_protein

import global_vars
global_vars.init()

winning_score = 0
winning_coordinates = global_vars.coordinates[:]

def algo_brute_force():

    current_score = 0

    def recursive_function(depth):



        current_score = score()
        global winning_score
        if current_score < winning_score:
            winning_score = current_score
            winning_coordinates = global_vars.coordinates[:]

            print("\n\nBest so far, stability of " + str(winning_score) + ":\n")
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

    if input("This brute force algorithm will take " + str(steps) + " steps. \nThat equals approx. "+ str(int(steps / (2684 * 60))) +"m "+ str(round(60*((steps / (2684 * 60)) % 1), 2)) +"s.\n U sure? (y/n) ").upper() == "Y":
        print()

        # fold_all_right()
        recursive_function(depth)

        print("Best solution found with a stability of " + str(winning_score))
        print()

        global_vars.coordinates = winning_coordinates

    else:
        print("\nStopping program\n")
        exit(1)



def fold_all_right():
    for i in range(1, len(global_vars.protein_string) - 1):
        fold(i, "R")
