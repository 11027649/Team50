# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: print_protein. A function that prints the protein to the screen.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import amino

import global_vars
global_vars.init()

def print_protein():
    """ Prints the grid in which the protein lays. """

    rows = len(grid[0])
    columns = len(grid)

    # get grid, print heigth and width to the screen
    grid = global_vars.grid
<<<<<<< HEAD
    # print("Height grid: " + str(len(grid[0])))
    # print("Width grid: " + str(len(grid)), end="\n\n")
=======
    print("Height grid: " + str(rows))
    print("Width grid: " + str(columns), end="\n\n")

    # iterate over rows
    for j in range(rows):
>>>>>>> c151632ddca14cc3ec9fe96b3c53374ca36db0d1

        # iterate over columns
        for i in range(columns):

            # print spaces on empty grid spots
            if (grid[i][j] == 0):
                print(" ", end=" ")
<<<<<<< HEAD
=======

            # print letters on grid spots where amino acids are
>>>>>>> c151632ddca14cc3ec9fe96b3c53374ca36db0d1
            else:
                print(grid[i][j].letter, end=" ")

        # print enter for next row
        print()

    # print enter after grid
    print()

    for j in range(len(grid[0])):

        for i in range(len(grid)):
            if (grid[i][j] == 0):
                print(" ", end=" ")
            else:
                print(grid[i][j].num_id, end=" ")

        print()

    print()
