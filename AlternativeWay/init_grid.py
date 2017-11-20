# init_grid

# initializes grid and drops protein in it
from global_vars import amino

import global_vars
global_vars.init()

def init_grid():

    protein_string = global_vars.protein_string
    protein_length = len(protein_string)

    grid = global_vars.grid
    coordinates = global_vars.coordinates

    grid = [[amino(i, protein_string[i], i, 0) for j in range(1)] for i in range(protein_length)]

    coordinates = [[i ,0] for i in range(protein_length)]

    global_vars.grid = grid
    global_vars.coordinates = coordinates
