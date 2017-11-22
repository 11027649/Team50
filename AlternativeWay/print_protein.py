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
                print(grid[i][j].num_id, end=" ")

        print()

    print()

def fancy_print():
    # get grid, print heigth and width to the screen
    grid = global_vars.grid

    # gets the length of the old grid
    x_old = len(grid)
    y_old = len(grid[0])

    # gets the length of the new grid
    x_new = (x_old * 2) + 4
    y_new = (y_old * 2) + 4

    # init the printgrid
    printgrid = [['  ' for i in range(y_new)] for j in range(x_new)]

    # putt all proteins in the string
    for i in range(len(global_vars.protein_string)):
        coor_x = (global_vars.coordinates[i][0] * 2) + 2
        coor_y = (global_vars.coordinates[i][1] * 2) + 2
        printgrid[coor_x][coor_y] = global_vars.grid[(coor_x - 2) / 2][(coor_y - 2) / 2]
    # add layout to the grid
    for i in range(len(global_vars.protein_string)):
        coor_x = global_vars.coordinates[i][0] * 2
        coor_y = global_vars.coordinates[i][1] * 2
        if not printgrid[coor_x][coor_y] == '  ' and printgrid[coor_x][coor_y + 2].num_id == i + 1:
            printgrid[coor_x][coor_y + 1] = '| '
        elif not printgrid[coor_x][coor_y] == '  ' and printgrid[coor_x][coor_y - 2].num_id == i + 1:
            printgrid[coor_x][coor_y - 1] = '| '
        elif not printgrid[coor_x][coor_y] == '  ' and printgrid[coor_x + 2][coor_y].num_id == i + 1:
            printgrid[coor_x + 1][coor_y] = '- '
        elif not printgrid[coor_x][coor_y] == '  ' and printgrid[coor_x - 2][coor_y].num_id == i + 1:
            printgrid[coor_x - 1][coor_y] = '- '

    for j in range(y_new):
        for i in range(x_new):
            if not str(type(printgrid[i][j])) == "<class 'str'>":
                if printgrid[i][j].letter == 'H':
                    print(printgrid[i][j].letter, end='')
                elif printgrid[i][j].letter =='P':
                    print(printgrid[i][j].letter, end='')
            else:
                print(printgrid[i][j], end = '')
        print()
