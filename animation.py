import time
import os

def visualize_protein(grid, protein):
    """ Prints the protein with nicely added layout to make it easy to see
        where the bonds of the protein are. """
    # gets the length of the old grid
    x_old = len(grid)
    y_old= len(grid[0])
    # makes the length of the new grid twice as large
    x_new = (2*x_old)
    y_new = (2*y_old)

    # make a grid twice the size of the former grid
    printgrid = [['  ' for p in range(y_new)] for q in range(x_new)]

    for i in range(len(protein)):
        # puts letters in the right coordinates
        coor_x = (protein[i].aa_x ) * 2
        coor_y = (protein[i].aa_y ) * 2
        print(coor_x)
        print(coor_y)
        # the coordinates are
        printgrid[coor_x][coor_y] = protein[i]

    # add layout, making the grid 2 times as big, to add bonds
        # print extra layout for all AA except the last one
        if i != (len(protein)) - 1:

            # pipeline under the letter
            if protein[i].direction == 0:
                printgrid[coor_x][coor_y - 1] = '| '

            # stripes right to it
            elif protein[i].direction == 1:
                printgrid[coor_x + 1][coor_y] = '---'

            # pipeline above it
            elif protein[i].direction == 2:
                printgrid[coor_x][coor_y + 1] = '| '

            # stripes left to it
            elif protein[i].direction == 3:
                printgrid[coor_x - 1][coor_y] = '---'

    # print the grid
    for i in range(y_new):
        print("    ", end='')

        # print rows
        for j in range(x_new):
            if not printgrid[j][i] == '  ' and not printgrid[j][i] ==  '---' and not printgrid[j][i] == '| '  :
                print(printgrid[j][i])
                # print H blue
                if printgrid[j][i].letter == 'H':
                    print('\033[34;1m' + printgrid[j][i].letter + '\033[0m', end='')


                    if printgrid[j][i].direction != 1 and j + 1 < x_new - 1 and printgrid[j + 1][i] != "---":
                        print(' ', end='')
                # print P red
                elif printgrid[j][i].letter == 'P':
                    print('\033[31;1m' + printgrid[j][i].letter + '\033[0m', end='')


                    if printgrid[j][i].direction != 1 and j + 1 < x_new - 1 and printgrid[j + 1][i] != "---":
                        print(' ', end='')
                # if something else is present
                else:
                    print(printgrid[j][i], end='')

            print()
        print()


def clear_screen():
    """ Clears the screen to show how the protein folds in a nice way. """

    # sleep a little for animation's sake
    time.sleep(1)

    # clear the terminal window
    os.system("cls")
