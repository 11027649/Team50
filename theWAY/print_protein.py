# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: print_protein. A function that prints the protein to the screen.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from global_vars import amino

import global_vars
global_vars.init()

from colorama import init
init()

class color:
   BLUE = '\033[94m'
   ORANGE = '\033[93m'
   RED = '\033[91m'
   GREY = '\033[33m'
   FIRST = '\033[4m'
   END = '\033[0m'

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

def fancy_print_protein(show_bonds = ''):

    print()

    # get grid, print heigth and width to the screen

    grid = global_vars.grid
    coordinates = global_vars.coordinates

    fancy_grid_height = len(grid[0]) * 2
    fancy_grid_width = len(grid) * 2


    fancy_grid = [["  " for j in range(fancy_grid_height)] for i in range(fancy_grid_width)]



    # put all the aminos at the right location and the layout
    for i in range(len(global_vars.protein_string)):
        # calculate the coordinates for the new grid and put it in the new grid
        current_coordinates = [coordinates[i][0] * 2, coordinates[i][1] * 2]

        fancy_grid[current_coordinates[0]][current_coordinates[1]] = grid[coordinates[i][0]][coordinates[i][1]]

        # if down is an amino
        if current_coordinates[1] - 2 >= 0:
            if type(fancy_grid[current_coordinates[0]][current_coordinates[1] - 2]) == amino:
                # if id is one lower add the layout
                if fancy_grid[current_coordinates[0]][current_coordinates[1] - 2].num_id == i - 1:
                    fancy_grid[current_coordinates[0]][current_coordinates[1] - 1] = '| '
                # if not one lower print the bond
                elif fancy_grid[current_coordinates[0]][current_coordinates[1] - 2].letter == fancy_grid[current_coordinates[0]][current_coordinates[1]].letter:
                    if not fancy_grid[current_coordinates[0]][current_coordinates[1]].letter == 'P':
                        fancy_grid[current_coordinates[0]][current_coordinates[1] - 1] = ': '

        # if there is up an amino
        if current_coordinates[1] + 2 < fancy_grid_height:
            if type(fancy_grid[current_coordinates[0]][current_coordinates[1] + 2]) == amino:
                if fancy_grid[current_coordinates[0]][current_coordinates[1] + 2].num_id == i - 1:
                    fancy_grid[current_coordinates[0]][current_coordinates[1] + 1] = '| '
                elif fancy_grid[current_coordinates[0]][current_coordinates[1] + 2].letter == fancy_grid[current_coordinates[0]][current_coordinates[1]].letter:
                    if not fancy_grid[current_coordinates[0]][current_coordinates[1]].letter == 'P':
                        fancy_grid[current_coordinates[0]][current_coordinates[1] + 1] = ': '

        # if there is left an amino
        if current_coordinates[0] - 2 >= 0:

            if type(fancy_grid[current_coordinates[0] - 2][current_coordinates[1]]) == amino:
                # if id is one lower add the layout
                if fancy_grid[current_coordinates[0] - 2][current_coordinates[1]].num_id == i - 1:
                    fancy_grid[current_coordinates[0] - 1][current_coordinates[1]] = '---'
                # if not one lower print the bond
                elif fancy_grid[current_coordinates[0] - 2][current_coordinates[1]].letter == fancy_grid[current_coordinates[0]][current_coordinates[1]].letter:
                    if not fancy_grid[current_coordinates[0]][current_coordinates[1]].letter == 'P':
                        fancy_grid[current_coordinates[0] - 1][current_coordinates[1]] = '...'
        # if there is right an amino
        if current_coordinates[0] + 2 < fancy_grid_width:
            if type(fancy_grid[current_coordinates[0] + 2][current_coordinates[1]]) == amino:
                # if id is one lower add the layout
                if fancy_grid[current_coordinates[0] + 2][current_coordinates[1]].num_id == i - 1:
                    fancy_grid[current_coordinates[0] + 1][current_coordinates[1]] = '---'
                # if not one lower print the bond
                elif fancy_grid[current_coordinates[0] + 2][current_coordinates[1]].letter == fancy_grid[current_coordinates[0]][current_coordinates[1]].letter:
                    if not fancy_grid[current_coordinates[0]][current_coordinates[1]].letter == 'P':
                        fancy_grid[current_coordinates[0] + 1][current_coordinates[1]] = '...'




    for j in range(fancy_grid_height):

        for i in range(fancy_grid_width):

            if type(fancy_grid[i][j]) == str:
                if fancy_grid[i][j] == "..." or fancy_grid[i][j] == ": ":
                    print(color.GREY + fancy_grid[i][j] + color.END, end='')
                else:
                    print(fancy_grid[i][j], end='')
            else:
                if fancy_grid[i][j].num_id == 0:
                    if fancy_grid[i][j].letter == "H":
                        print(color.BLUE + color.FIRST + fancy_grid[i][j].letter + color.END, end = '')
                    elif fancy_grid[i][j].letter == "P":
                        print(color.RED + color.FIRST + fancy_grid[i][j].letter + color.END, end = '')
                    elif fancy_grid[i][j].letter == "C":
                        print(color.ORANGE + color.FIRST + fancy_grid[i][j].letter + color.END, end = '')
                elif fancy_grid[i][j].letter == "H":
                    print(color.BLUE + fancy_grid[i][j].letter + color.END, end = '') #BLUE
                elif fancy_grid[i][j].letter == "P":
                    print(color.RED + fancy_grid[i][j].letter + color.END, end = '') #RED
                elif fancy_grid[i][j].letter == "C":
                    print(color.ORANGE + fancy_grid[i][j].letter + color.END, end = '') #Orange
                else:
                    print(fancy_grid[i][j].letter, end = '') #Black

            if i < fancy_grid_width - 1 and not fancy_grid[i][j] == "| " \
            and not fancy_grid[i][j] == ": " and (not type(fancy_grid[i + 1][j]) == str or fancy_grid[i + 1][j] == "  ") \
            and not fancy_grid[i][j] == "---" and not fancy_grid[i][j] == "..." and not fancy_grid[i][j] == "  ":
                print(" ", end='')

        print()

    print()
