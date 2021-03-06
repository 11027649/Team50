# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: update_grid()
#
# A function that updates what is in the grid by taking the global variables
# coordinates and protein string.
# Takes: global var coordinates, protein and grid
# Updates: global var coordinates and grid.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def update_grid(protein):
    """ Gets the global coordinates and uses them to get the grid and heigth for
        the grid. Corrects these coordinates to make them as low as possible.
        Initializes the grid.  """

    # get coordinates
    coor = protein.coordinates[:]

    # initiate min and max coordinates
    xmax = xmin = coor[0][0]
    ymax = ymin = coor[0][1]
    zmax = zmin = coor[0][2]

    # get the right min and max coordinates
    for i in range(1, len(protein.protein_string)):
        if coor[i][0] > xmax:
            xmax = coor[i][0]
        elif coor[i][0] < xmin:
            xmin = coor[i][0]
        
        if coor[i][1] > ymax:
            ymax = coor[i][1]
        elif coor[i][1] < ymin:
            ymin = coor[i][1]

        if coor[i][2] > zmax:
            zmax = coor[i][2]
        elif coor[i][2] < zmin:
            zmin = coor[i][2]

    # correct all the coordinates of the AA's with xmin, ymin and zmin
    for i in range(protein.length):
        coor[i][0] -= xmin
        coor[i][1] -= ymin
        coor[i][2] -= zmin

    # initialize the grid heigth and width, and make the grid
    grid_x = xmax - xmin + 1
    grid_y = ymax - ymin + 1
    grid_z = zmax - zmin + 1
    
    protein.grid = [[[0 for i in range(grid_z + 1)] for j in range(grid_y + 1)] for k in range(grid_x + 1)]

    # put the right AA's at the grid points
    for i in range(protein.length):
        protein.grid[coor[i][0]][coor[i][1]][coor[i][2]] = protein.aminos[i]

    # put the new coordinates in the global coordinates
    protein.coordinates = coor[:]

    return protein
