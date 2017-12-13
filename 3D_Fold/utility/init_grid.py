# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: init_grid.
#
# A function that initializes the grid and puts the protein in it.
# Takes: global vars protein_string, grid and coordinates.
# Updates: global vars grid and coordinates
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from protein_class import Amino

def init_grid(protein):
    """ Lays the protein horizontally in a grid of heigth 1. """

	# get global protein string and save it's length
    protein_string = protein.protein_string
    protein_length = protein.protein_length

    # initialize the grid
    grid = [[[0 for i in range(2)] for j in range(2)] for k in range(protein_length + 1)]
    
    # put aminos in grid
    for i in range(protein_length):
        grid[i][0][0] = Amino(i, protein_string[i])

    # update coordinates
    coordinates = [[i ,0, 0] for i in range(protein_length)]

    # put grid and coordinates in protein
    protein.grid = grid
    protein.coordinates = coordinates

    return protein
