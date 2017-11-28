# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: print_protein. A function that prints the protein to the screen.
#
# Contains: fancy_print_protein. A function that makes a new grid with layout.
# The layout depends on the users input. Depending on the users input
# fancy_grid_Bonds or fancy_grid_noBonds is used for adding the layout.
# This new grid will be printed by this function.
#
# fancy_grid_Bonds: A function to add layout to the new grid without showing
# bonds that add to the score.
#
# fancy_grid_noBonds: A function to add layout to the new grid and shows
# bonds that add to the score.
#
# Both fancy_grid_Bonds and fancy_grid_noBonds take and return:
# Take: fancy_grid, grid, coordinates
# Return: fancy_grid
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

def fancy_print_protein():
    """ Prints how the protein is folded with layout and colors. """
    print()

    # get grid, coordinates, print heigth and width to the screen

    grid = global_vars.grid
    coordinates = global_vars.coordinates
    fancy_grid_height = len(grid[0]) * 2
    fancy_grid_width = len(grid) * 2

    # initialize an empty grid
    fancy_grid = [["  " for j in range(fancy_grid_height)] for i in range(fancy_grid_width)]

    # will fill the grid with layout depending on the answer of the user
    if input("Do you wish to show the bonds? (y/n) ").upper() == "Y":
        fancy_grid = fancy_grid_Bonds(fancy_grid, grid, coordinates)
    else:
        fancy_grid= fancy_grid_noBonds(fancy_grid, grid, coordinates)


    # iterates over the grid and prints with the right colors
    for j in range(fancy_grid_height):

        for i in range(fancy_grid_width):

            # if it is a string print the string
            if type(fancy_grid[i][j]) == str:
                if fancy_grid[i][j] == "..." or fancy_grid[i][j] == ": ":
                    print(color.GREY + fancy_grid[i][j] + color.END, end='')
                else:
                    print(fancy_grid[i][j], end='')

            # if it is an amino add the correct layout
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


def fancy_grid_noBonds(fancy_grid, grid, coordinates):
    """ will fill the fancy_grid with layout without showing the bonds that add to the score """

    # initialize some variables
    fancy_grid_height = len(grid[0]) * 2
    fancy_grid_width = len(grid) * 2

    # iterate over the protein and add the layout
    for i in range(len(global_vars.protein_string)):

        # places the aminos in the new grid with empty cells between them
        current_coordinates = [coordinates[i][0] * 2, coordinates[i][1] * 2]
        fancy_grid[current_coordinates[0]][current_coordinates[1]] = grid[coordinates[i][0]][coordinates[i][1]]

        # as long as there is a previous amino add layout between the currentand previous coordinates
        if i > 0:
            previous_coordinates = [coordinates[i - 1][0] * 2, coordinates[i - 1][1] * 2]

            # if the previous was left
            if previous_coordinates[0] == current_coordinates[0] - 2:
                fancy_grid[current_coordinates[0] - 1][current_coordinates[1]] = '---'

                # if the previous was right
            elif previous_coordinates[0] == current_coordinates[0] + 2:
                fancy_grid[current_coordinates[0] + 1][current_coordinates[1]] = '---'

                # if the previous was up
            elif previous_coordinates[1] == current_coordinates[1] + 2:
                fancy_grid[current_coordinates[0]][current_coordinates[1] + 1] = '| '

                # if the previous was down
            elif previous_coordinates[1] == current_coordinates[1] - 2:
                fancy_grid[current_coordinates[0]][current_coordinates[1] - 1] = '| '


    return fancy_grid
def fancy_grid_Bonds(fancy_grid, grid, coordinates):
    """ will fill the fancy_grid with layout and shows the bonds that add to the score """

    # initialize some variables
    fancy_grid_height = len(grid[0]) * 2
    fancy_grid_width = len(grid) * 2

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

                # if id is one lower add the layout
                if fancy_grid[current_coordinates[0]][current_coordinates[1] + 2].num_id == i - 1:
                    fancy_grid[current_coordinates[0]][current_coordinates[1] + 1] = '| '

                # if not one lower print the bond
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
    return fancy_grid
