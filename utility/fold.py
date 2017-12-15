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
from protein_class import Amino

import numpy as np
import copy

def fold(num_id, direction, protein):
    """ Finds an origin to fold around and multiplies the coordinates of the aminos
        that will get a different place with a rotation matrix to get the new
        coordinates. If the fold is not possible, returns and old grid and at which
        amino acid this fold was colliding. """

    coordinates = protein.coordinates
    backup_coordinates = coordinates[:]
    grid = protein.grid

    protein_length = protein.length
    grid_x = len(grid)
    grid_y = len(grid[0])
    grid_z = len(grid[0][0])
    # print("IN FOLD, x, y, z: ", grid_x, grid_x, grid_z)

    length = protein_length
    if num_id >= length or num_id < 1:
        print("You try to fold on " + str(num_id) + ", only up to id " + str(length - 1) + " available.")

    if num_id >= protein_length or num_id < 1:
        print("This fold index doesn't exist.")

        # returncode 2: an invalid place to fold
        return "out of range"

    # find the rotation origin and print it's coordinates
    rot_origin = [coordinates[num_id][0], coordinates[num_id][1], coordinates[num_id][2]]

    # print("Pivot origin: ", rot_origin[0], ",", rot_origin[1], ",", rot_origin[2])

    # rotations matrixes around z axis
    rotation_matrix_down_z = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    rotation_matrix_up_z = [[0, 1, 0], [-1, 0, 0],[0, 0, 1]]

    # rotations around y axis
    rotation_matrix_down_y = [[0, 0, -1], [0, 1, 0],[1, 0, 0]]
    rotation_matrix_up_y = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]

    # rotations around x axis
    rotation_matrix_down_x = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
    rotation_matrix_up_x = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]

    returncode = False

    # determine the axis of rotations
    next_coords = [coordinates[num_id + 1][0], coordinates[num_id + 1][1], coordinates[num_id + 1][2]]

    axis = ""

    if (next_coords[0] != rot_origin[0]):
        if (direction == "R"):
            rotation_matrix = rotation_matrix_up_z
        elif (direction == "L"):
            rotation_matrix = rotation_matrix_down_z
        elif (direction == "U"):
            rotation_matrix = rotation_matrix_up_y
        elif (direction == "D"):
            rotation_matrix = rotation_matrix_down_y

    elif (next_coords[1] != rot_origin[1]):
        if (direction == "R"):
            rotation_matrix = rotation_matrix_up_z
        elif (direction == "L"):
            rotation_matrix = rotation_matrix_down_z
        elif (direction == "U"):
            rotation_matrix = rotation_matrix_up_x
        elif (direction == "D"):
            rotation_matrix = rotation_matrix_down_x

    elif (next_coords[2] != rot_origin[2]):
        if (direction == "R"):
            rotation_matrix = rotation_matrix_up_y
        elif (direction == "L"):
            rotation_matrix = rotation_matrix_down_y
        elif (direction == "U"):
            rotation_matrix = rotation_matrix_up_x
        elif (direction == "D"):
            rotation_matrix = rotation_matrix_down_x

    # iterates over the aminos, beginning at the one after the amino acid where
    # we'll fold
    for i in range(num_id + 1, protein_length):

        # cleans all aminos from where we'll fold
        grid[coordinates[i][0]][coordinates[i][1]][coordinates[i][2]] = 0

    # iterates over the aminos, beginning at the one after where we'll fold
    for i in range(num_id + 1, protein_length):

        from_coords = coordinates[i]

        subtracted = np.subtract(from_coords, rot_origin)
        to_coords = np.dot(rotation_matrix, subtracted) + rot_origin

        # expand grid if the fold made the protein to big to fit, and detect
        # foldings that aren't possible
        if (to_coords[0] < 0 or to_coords[0] >= grid_x):
            coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

        elif (to_coords[1] < 0 or to_coords[1] >= grid_y):
            coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

        elif (to_coords[2] < 0 or to_coords[2] >= grid_z):
            coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

        # if fold isn't possible
        elif (str(type(grid[to_coords[0]][to_coords[1]][to_coords[2]])) == "<class 'protein_class.Amino'>"):
            # print("Collision detected while folding amino " + str(num_id) + "\n -> Stopped this fold, cause amino " + str(i) + " was colliding")
            coordinates = backup_coordinates[:]
            returncode = True
            break

        else:
            coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

    # update global coordinates and update the grid
    protein.coordinates = coordinates[:]
    update_grid(protein)

    if returncode == True:
        return ["collision", protein]
    else:
        return [0, protein]
