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

    fancy_grid_height = len(grid[0]) * 2
    fancy_grid_width = len(grid) * 2


    fancy_grid = [["  " for j in range(fancy_grid_height)] for i in range(fancy_grid_width)]

    print (coordinates)

    print(fancy_grid_width, end = 'FG WIDTH')
    print(fancy_grid_height, end = 'FG HEIGHT')
    # put all the aminos at the right location and the layout
    for i in range(len(global_vars.protein_string)):
        # calculate the coordinates for the new grid and put it in the new grid
        current_coordinates = [coordinates[i][0] * 2, coordinates[i][1] * 2]
        print(str(i) + "LOOP")
        print(current_coordinates[0])
        print(current_coordinates[1])
        print(grid[coordinates[i][0]][0])
        print(grid[0][coordinates[i][1]])
        fancy_grid[current_coordinates[0]][current_coordinates[1]] = grid[coordinates[i][0]][coordinates[i][1]]

        # if there is a previous amino acid add the correspondending layout
        if i > 0:
            previous_coordinates = [coordinates[i - 1][0] * 2, coordinates[i - 1][1] * 2]

            # if the previous was left
            if previous_coordinates[0] == current_coordinates[0] - 2:
                # the current x coordinate - 1 will become the right layout
                fancy_grid[current_coordinates[0] - 1][current_coordinates[1]] = '--'
            # if the previous was right
            elif previous_coordinates[0] == current_coordinates[0] + 2:
                fancy_grid[current_coordinates[0] + 1][current_coordinates[1]] = '--'

            # if the previous was up
            elif previous_coordinates[1] == current_coordinates[1] + 2:
                fancy_grid[current_coordinates[0]][current_coordinates[1] + 1] ='| '
            # if the previous was down
            elif previous_coordinates[1] == current_coordinates[1] -2:
                fancy_grid[current_coordinates[0]][current_coordinates[1] - 1] ='| '









    for j in range(fancy_grid_height):

        for i in range(fancy_grid_width):
            if type(fancy_grid[i][j]) == str:
                print(fancy_grid[i][j], end='')
            else:
                print("" + fancy_grid[i][j].letter + "", end = ' ')

        print()

    print()
