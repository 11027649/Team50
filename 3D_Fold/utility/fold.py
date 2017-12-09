# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: fold. A function that folds a protein. Does this by finding an
# origin and rotating the rest of the protein with a rotation matrix (left or
# right), depending on the direction in which the protein is being fold.
#
# Takes: num_id and direction, global vars coordinates, grid and protein_string
# Updates: global var coordinates
# Calls: update_grid()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from utility.update_grid import update_grid
from global_vars import Amino

import global_vars
global_vars.init()

import numpy as np

def fold(num_id, direction):
    """ Finds an origin to fold around and multiplies the coordinates of the aminos
        that will get a different place with a rotation matrix to get the new
        coordinates. If the fold is not possible, returns and old grid and at which
        amino acid this fold was colliding. """

    coordinates = global_vars.protein.coordinates
    backup_coordinates = coordinates[:]
    grid = global_vars.grid

    protein_length = len(global_vars.protein.protein_string)
    grid_height = len(grid[0])
    grid_width = len(grid)

    length = protein_length
    if num_id >= length or num_id < 1:
        print("You try to fold on " + str(num_id) + ", only up to id " + str(length - 1) + " available.")

    if num_id >= protein_length or num_id < 1:
        print("This fold index doesn't exist.")

        # returncode 2: an invalid place to fold
        return "out of range"

    # find the rotation origin and print it's coordinates
    rot_origin = [coordinates[num_id][0], coordinates[num_id][1], coordinates[num_id][2]]

    print("Pivot origin: ", rot_origin[0], ",", rot_origin[1], ",", rot_origin[2])

    # set up rotation matrices
    rotation_matrix_left = [[0, 1, 0], [-1, 0, 0],[0, 0, 1]]
    rotation_matrix_right = [[0, -1, 0], [1, 0, 0],[0, 0, -1]]
    # rotation_matrix_down =
    # rotation_matrix_up = 

    returncode = False

    # for folds to Left or Right, set up the right rotation matrix
    if(direction == "R"):
        rotation_matrix = rotation_matrix_right
    elif(direction == "L"):
        rotation_matrix = rotation_matrix_left

    for_range = range(num_id + 1, protein_length)

    # iterates over the aminos, beginning at the one after the amino acid where
    # we'll fold
    for i in for_range:

        # cleans all aminos from where we'll fold
        grid[coordinates[i][0]][coordinates[i][1]][coordinates[i][2]] = 0

    # iterates over the aminos, beginning at the one after where we'll fold
    for i in for_range:

        from_coords = coordinates[i]
        print(rotation_matrix, from_coords, rot_origin)
        subtracted = np.subtract(from_coords, rot_origin)
        to_coords = np.dot(rotation_matrix, subtracted) + rot_origin

        # expand grid if the fold made the protein to big to fit, and detect
        # foldings that aren't possible
        if (to_coords[0] < 0 or to_coords[0] >= grid_width):
            coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

        elif (to_coords[1] < 0 or to_coords[1] >= grid_height):
            coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

        elif (str(type(grid[to_coords[0]][to_coords[1]])) == "<class 'global_vars.Amino'>"):
            # print("Collision detected while folding amino " + str(num_id) + "\n -> Stopped this fold, cause amino " + str(i) + " was colliding")
            coordinates = backup_coordinates
            returncode = True
            break

        else:
            coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

    # update global coordinates and update the grid
    global_vars.coordinates = coordinates
    update_grid()

    if returncode == True:
        return "collision"
    else:
        return 0
