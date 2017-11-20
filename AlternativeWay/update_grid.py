# make_grid.py. Allows user to make the grid from a string
# global_vars.protein_string
from global_vars import amino

import global_vars
global_vars.init()

def update_grid():

    coordinates = global_vars.coordinates

    xmax = xmin = coordinates[0][0]
    ymax = ymin = coordinates[0][1]

    for i in range(1, len(global_vars.protein_string)):
        if coordinates[i][0] > xmax:
            xmax = coordinates[i][0]
        elif coordinates[i][0] < xmin:
            xmin = coordinates[i][0]
        if coordinates[i][1] > ymax:
            ymax = coordinates[i][1]
        elif coordinates[i][1] < ymin:
            ymin = coordinates[i][1]

    for i in range(len(global_vars.protein_string)):
        coordinates[i][0] -= xmin
        coordinates[i][1] -= ymin


    grid_width = xmax - xmin + 1
    grid_height = ymax - ymin + 1

    global_vars.grid = [[0 for j in range(grid_height)] for i in range(grid_width)]


    for i in range(len(coordinates)):
        global_vars.grid[coordinates[i][0]][coordinates[i][1]] = amino(i, global_vars.protein_string[i], coordinates[i][0], coordinates[i][1])

    global_vars.coordinates = coordinates
