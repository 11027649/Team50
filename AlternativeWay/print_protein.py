# print_protein.py

from global_vars import amino

import global_vars
global_vars.init()

def print_protein():

    grid = global_vars.grid
    print("Height grid: " + str(len(grid[0])))
    print("Width grid: " + str(len(grid)), end="\n\n")

    for j in range(len(grid[0])):

        for i in range(len(grid)):
            if (grid[i][j] == 0):
                print(".", end=" ")
            else:
                print(grid[i][j].letter, end=" ")

        print()

    print()
