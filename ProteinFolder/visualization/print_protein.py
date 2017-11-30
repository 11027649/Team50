# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: print_protein. A function that prints the protein to the screen.
#
# Contains: print_print_protein. A function that makes a new grid with layout.
# This new grid will be printed by this function.
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
    """ Prints how the protein is folded with layout, colors and bonds. """
    print()

    # get grid, coordinates, print heigth and width to the screen

    grid = global_vars.grid
    coordinates = global_vars.coordinates
    print_grid_height = len(grid[0]) * 2
    print_grid_width = len(grid) * 2

    # initialize an empty grid
    print_grid = [["  " for j in range(print_grid_height)] for i in range(print_grid_width)]

    # put all the aminos at the right location and the layout
    for i in range(len(global_vars.protein_string)):

        # calculate the coordinates for the new grid and put it in the new grid
        current_coordinates = [coordinates[i][0] * 2, coordinates[i][1] * 2]
        print_grid[current_coordinates[0]][current_coordinates[1]] = grid[coordinates[i][0]][coordinates[i][1]]

        print_grid = add_layout(current_coordinates, print_grid, i, print_grid_height, print_grid_width)


    # iterates over the grid and prints with the right colors
    for j in range(print_grid_height):

        for i in range(print_grid_width):

            # if it is a string print the string
            if type(print_grid[i][j]) == str:
                if print_grid[i][j] == "..." or print_grid[i][j] == ": ":
                    print(color.GREY + print_grid[i][j] + color.END, end='')
                else:
                    print(print_grid[i][j], end='')

            # if it is an amino add the correct layout
            else:
                if print_grid[i][j].letter == "H":
                    print(color.BLUE + print_grid[i][j].letter + color.END, end = '') #BLUE
                elif print_grid[i][j].letter == "P":
                    print(color.RED + print_grid[i][j].letter + color.END, end = '') #RED
                elif print_grid[i][j].letter == "C":
                    print(color.ORANGE + print_grid[i][j].letter + color.END, end = '') #Orange
                else:
                    print(print_grid[i][j].letter, end = '') #Black

            if i < print_grid_width - 1 and not print_grid[i][j] == "| " \
            and not print_grid[i][j] == ": " and (not type(print_grid[i + 1][j]) == str or print_grid[i + 1][j] == "  ") \
            and not print_grid[i][j] == "---" and not print_grid[i][j] == "..." and not print_grid[i][j] == "  ":
                print(" ", end='')

        print()

    print()


def add_layout(current_coordinates, print_grid, i, print_grid_height, print_grid_width):

    for index in range(4):

        info = [[[0, 2], current_coordinates[1], print_grid_height, -1, ["| ", ": "]], \
                        [[0, -2], current_coordinates[1], -1, 1, ["| ", ": "]], \
                        [[2, 0], current_coordinates[0], print_grid_width, -1, ["---", "..."]], \
                        [[-2, 0], current_coordinates[0], -1, 1, ["---", "..."]]]

        # if down is an amino
        if info[index][3] * (info[index][1] + info[index][0][0] + info[index][0][1]) > info[index][3] * info[index][2]:
            if type(print_grid[current_coordinates[0] + info[index][0][0]][current_coordinates[1] + info[index][0][1]]) == amino:
                # if id is one lower add the layout
                if print_grid[current_coordinates[0] + info[index][0][0]][current_coordinates[1] + info[index][0][1]].num_id == i - 1:
                    print_grid[current_coordinates[0] + int(0.5 * info[index][0][0])][current_coordinates[1] + int(0.5 * info[index][0][1])] = info[index][4][0]

                # if not one lower print the bond
                elif print_grid[current_coordinates[0] + info[index][0][0]][current_coordinates[1] + info[index][0][1]].letter == print_grid[current_coordinates[0]][current_coordinates[1]].letter:
                    if not print_grid[current_coordinates[0]][current_coordinates[1]].letter == 'P':
                        print_grid[current_coordinates[0] + int(0.5 * info[index][0][0])][current_coordinates[1] + int(0.5 * info[index][0][1])] = info[index][4][1]



    return print_grid
