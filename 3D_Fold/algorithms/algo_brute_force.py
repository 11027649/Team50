# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: brute_force, foldings_recursive.
#
# The algo_brute_force tries every foldation of the protein (multiple times for
# for now ;-P).
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import Amino
from utility.score import score
from utility.fold import fold

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

    length = len(global_vars.protein.protein_string)
    depth = length - 2
    steps = pow(3, len(global_vars.protein.protein_string) - 2)
    sps = 3000
    # initialize winning grid and coordinates to make sure they are not empty
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

    if input("This brute force algorithm will take " + str(steps) + " steps. \nThat equals approx. "+ str(int(steps / (sps * 60))) +"m "+ str(round(60*((steps / (sps * 60)) % 1), 2)) +"s.\n Are you sure you want to start? (y/n) ").upper() == "Y":
        print()

        start = time.time()
        foldings_recursive(depth)

        end = time.time()

        print("Best solution found with a stability of " + str(global_vars.protein.winning_score) + " in: " + str(int((end - start) / 60)) + "m " + str(round(((end - start) % 60), 2)) + "s.")
        print()

        # save winning coordinates and grid
        global_vars.grid = copy.deepcopy(global_vars.winning_grid)
        global_vars.protein.coordinates = copy.deepcopy(global_vars.protein.winning_coordinates)

        print(global_vars.protein.winning_coordinates)

    else:
        print("\nStopping program\n")
        exit(1)

# def foldings_recursive(depth):

#     protein_array
#     coordinates_array
#     directions_array

#     # check which i changed:
#         for i in range(j, length):
#             # make coordinates empty
#             corrdinates[i] =[]

#         # do the fold

#         current_coordinates = coordinates[i]
#         # give the coordinates again to the amino acid afther i
#         for i in range(j, length - 1):
#             coordinates[i + 1] = coordinates[i]

#             # x direction
#             if directions_array[i] == 0:
#                 coordinates[i + 1][0] = coordinates[i][0] + 1
#             elif directions_array[i] == 1:
#                 coordinates[i + 1][0] = coordinates[i][0] - 1

#             # y direction
#             elif directions_array[i] == 2:
#                 coordinates[i + 1][1] = coordinates[i][1] + 1
#             elif directions_array[i] == 3:
#                 coordinates[i + 1][1] = coordinates[i][1] - 1

#             # z direction
#             elif directions_array[i] == 4:
#                 coordinates[i + 1][2] = coordinates[i][1] + 1
#             elif directions_array[i] == 5:
#                 coordinates[i + 1][2] = coordinates[i][1] - 1


#             # set the amino at the right coordinates in the grid
#             x_coor = coordinates[i + 1][0]
#             y_coor = coordinates[i + 1][1]
#             Z_coor = coordinates[i + 1][2]
#             grid[x_coor][y_coor][z_coor]

#         # check score afther the grid is filled
#         score = score()
#         # safe the winning protein
#         if score < global_vars.protein.winning_score:
#             global_vars.protein.winning_score = score
#             global_vars.protein.winning_coordinates = coordinates
#             global_vars.protein.winning_grid = grid
