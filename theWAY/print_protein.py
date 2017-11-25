# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: print_protein. A function that prints the protein to the screen.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import amino

import global_vars
global_vars.init()

def print_protein():
    """ Prints the grid in which the protein lays. """

    # get grid, print heigth and width to the screen
    grid = global_vars.grid

    rows = len(grid[0])
    columns = len(grid)

    print("Height grid: " + str(rows))
    print("Width grid: " + str(columns), end="\n\n")

    # iterate over rows
    for j in range(rows):

        # iterate over columns
        for i in range(columns):

            # print spaces on empty grid spots
            if (grid[i][j] == 0):
                print(" ", end=" ")

            # print letters on grid spots where amino acids are
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
                if(grid[i][j].num_id > 9):
                    print(grid[i][j].num_id, end="")
                else:
                    print(grid[i][j].num_id, end=" ")

        print()

    print()

def fancy_print_protein():

    print("hoi")
    # get grid, print heigth and width to the screen

    grid = global_vars.grid
    coordinates = global_vars.coordinates

    print_protein()

    fancy_grid_width = len(grid[0]) * 2 - 1
    fancy_grid_height = len(grid) * 2 - 1
    print(fancy_grid_width, end = 'MAX X')
    print()
    print(fancy_grid_height, end = 'MAX Y')
    print()


    fancy_grid = [[" " for j in range(fancy_grid_height)] for i in range(fancy_grid_width)]





    for i in range(len(global_vars.protein_string)):
        current_coordinates = [coordinates[i][0] * 2, coordinates[i][1] * 2]
        previous_coordinates = []
        if i > 0:
            previous_coordinates = [coordinates[i - 1][0] * 2, coordinates[i - i][1] * 2]




        fancy_grid[current_coordinates[0]][current_coordinates[1]] = grid[coordinates[i][0]][coordinates[i][1]]



    for j in range(fancy_grid_height):

        for i in range(fancy_grid_width):
            print(j, end = "<y>")
            print(i, end = "<x>")
            if (grid[i][j] == 0):
                print(" ", end=" ")

            else:
                print(grid[i][j].num_id, end=" ")

        print()

    print()
