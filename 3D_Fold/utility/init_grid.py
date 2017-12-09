# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: init_grid.
#
# A function that initializes the grid and puts the protein in it.
# Takes: global vars protein_string, grid and coordinates.
# Updates: global vars grid and coordinates
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import Amino

import global_vars
global_vars.init()

def init_grid():
    """ Lays the protein horizontally in a grid of heigth 1. """

	# get global protein string and save it's length
    protein_string = global_vars.protein.protein_string
    protein_length = len(protein_string)

    # get global grid and coordinates, initialize grid
    grid = global_vars.grid
    coordinates = global_vars.protein.coordinates

    # initialize the grid with aminos, z, y, x
    grid = [[[0 for i in range(2)] for j in range(2)] for k in range(protein_length)]
    
    for i in range(protein_length - 1):
        grid[i][0][0] = Amino(i, protein_string[i])


    # update coordinates
    coordinates = [[i ,0, 0] for i in range(protein_length)]

    # put grid and coordinates back in global vars
    global_vars.grid = grid
    global_vars.protein.coordinates = coordinates
