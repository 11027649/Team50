# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: update_grid()
#
# A function that updates what is in the grid by taking the global variables
# coordinates and protein string.
# Takes: global var coordinates, protein and grid
# Updates: global var coordinates and grid.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import Amino

import global_vars
global_vars.init()

def update_grid():
    """ Gets the global coordinates and uses them to get the grid and heigth for
        the grid. Corrects these coordinates to make them as low as possible.
        Initializes the grid.  """

    # get coordinates
    coordinates = global_vars.protein.coordinates

    # initiate min and max coordinates
    xmax = xmin = coordinates[0][0]
    ymax = ymin = coordinates[0][1]
    zmax = zmin = coordinates[0][2]

    # get the right min and max coordinates
    for i in range(1, len(global_vars.protein.protein_string)):
        if coordinates[i][0] > xmax:
            xmax = coordinates[i][0]
        elif coordinates[i][0] < xmin:
            xmin = coordinates[i][0]
        
        if coordinates[i][1] > ymax:
            ymax = coordinates[i][1]
        elif coordinates[i][1] < ymin:
            ymin = coordinates[i][1]

        if coordinates[i][2] > zmax:
            zmax = coordinates[i][1]
        elif coordinates[i][2] < ymin:
            ymin = coordinates[i][1]

    # correct all the coordinates of the AA's with xmin, ymin and zmin
    for i in range(len(global_vars.protein.protein_string)):
        coordinates[i][0] -= xmin
        coordinates[i][1] -= ymin
        coordinates[i][2] -= zmin

    # initialize the grid heigth and width, and make the grid
    grid_width = xmax - xmin + 1
    grid_height = ymax - ymin + 1
    grid_breadth = zmax - zmin + 1
    
    global_vars.grid = [[[0 for i in range(grid_breadth + 1)] for j in range(grid_height + 1)] for k in range(grid_width + 1)]

    # put the right AA's at the grid points
    for i in range(len(global_vars.protein.protein_string)):
        print(i, coordinates[i], len(global_vars.protein.protein_string))
        global_vars.grid[coordinates[i][0]][coordinates[i][1]][coordinates[i][2]] = \
            Amino(i, global_vars.protein.protein_string[i])

    # put the new coordinates in the global coordinates
    ###### IT SEEMS THIS SENTENCE IS DOING NOTHING, BUT ISN'T IT WEIRD TO NOT UPDATE
    ###### THE COORDINATES?
    global_vars.protein.coordinates = coordinates
