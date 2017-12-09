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
    coor = global_vars.protein.coordinates[:]

    # initiate min and max coordinates
    xmax = xmin = coor[0][0]
    ymax = ymin = coor[0][1]
    zmax = zmin = coor[0][2]

    # get the right min and max coordinates
    for i in range(1, len(global_vars.protein.protein_string)):
        if coor[i][0] > xmax:
            xmax = coor[i][0]
        elif coor[i][0] < xmin:
            xmin = coor[i][0]
        
        if coor[i][1] > ymax:
            ymax = coor[i][1]
        elif coor[i][1] < ymin:
            ymin = coor[i][1]

        if coor[i][2] > zmax:
            zmax = coor[i][1]
        elif coor[i][2] < ymin:
            ymin = coor[i][1]

    # correct all the coordinates of the AA's with xmin, ymin and zmin
    for i in range(len(global_vars.protein.protein_string)):
        coor[i][0] -= xmin
        coor[i][1] -= ymin
        coor[i][2] -= zmin

    # initialize the grid heigth and width, and make the grid
    grid_x = xmax - xmin + 1
    grid_y = ymax - ymin + 1
    grid_z = zmax - zmin + 1
    
    global_vars.grid = [[[0 for i in range(grid_z + 1)] for j in range(grid_y + 1)] for k in range(grid_x + 1)]

    # put the right AA's at the grid points
    for i in range(len(global_vars.protein.protein_string)):
        print(i, coor[i][0], coor[i][1], coor[i][2])
        global_vars.grid[coor[i][0]][coor[i][1]][coor[i][2]] = Amino(i, global_vars.protein.protein_string[i])

    # put the new coordinates in the global coordinates
    global_vars.protein.coordinates = coor[:]
