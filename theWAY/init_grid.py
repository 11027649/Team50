# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: init_grid.
#
# A function that initializes the grid and puts the protein in it.
# Takes: global vars protein_string, grid and coordinates.
# Updates: global vars grid and coordinates
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import amino

import global_vars
global_vars.init()

def init_grid():
    """ Lays the protein horizontally in a grid of heigth 1. """

	# get global protein string and save it's length
    protein_string = global_vars.protein_string
    protein_length = len(protein_string)

    # get global grid and coordinates, initialize grid
    grid = global_vars.grid
    coordinates = global_vars.coordinates

    grid = [[amino(i, protein_string[i], i, 0) for j in range(1)] for i in range(protein_length)]

    # update coordinates
    coordinates = [[i ,0] for i in range(protein_length)]

    # put grid and coordinates back in global vars
    global_vars.grid = grid
    global_vars.coordinates = coordinates
