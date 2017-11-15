import time
import os

def print_protein(grid):
    """ Prints the protein with nicely added layout to make it easy to see
        where the bonds of the protein are. """
    
    # make a grid twice the size of the former grid
    grid = [['  ' for p in range(y * 2 - 1)] for q in range(x * 2 - 1)]

    print('this is min x en min y', end='')

    print(str(protein_length) + 'in visualize_fold')

    for i in range(protein_length):

        coor_x = (aa_info[i][0] ) * 2
        coor_y = (aa_info[i][1] ) * 2
        print(coor_x)
        print(coor_y)
        # the coordinates are
        grid[coor_x][coor_y] = aa_info[i][2]

    # add layout, making the grid 2 times as big, to add bonds
        # print extra layout for all AA except the last one
        if i != protein_length - 1:

            # pipeline under it
            if aa_info[i][3] == 0:
                grid[coor_x][coor_y - 1] = '| '

            # stripes right to it
            elif aa_info[i][3] == 1:
                grid[coor_x + 1][coor_y] = '---'

            # pipeline above it
            elif aa_info[i][3] == 2:
                grid[coor_x][coor_y + 1] = '| '

            # stripes left to it
            elif aa_info[i][3] == 3:
                grid[coor_x - 1][coor_y] = '---'

            print('klaar')

    # print the grid
    for i in range(y * 2 - 1):
        print("    ", end='')

        # print rows
        for j in range(x * 2 - 1):

                # print H blue
                if grid[j][i][0] == 'H':
                    print('\033[34;1m' + grid[j][i][0] + '\033[0m', end='')


                    if grid[j][i][1] != 1 and j + 1 < x * 2 - 1 and grid[j + 1][i] != "---":
                        print(' ', end='')

                    #if grid[j][i][1] != 1 and j + 1 < x * 2 - 1 and grid[j + 1][i] != "---":
                     #  print(' ', end='')


                # print P red
                elif grid[j][i][0] == 'P':
                    print('\033[31;1m' + grid[j][i][0] + '\033[0m', end='')


                    if grid[j][i][1] != 1 and j + 1 < x * 2 - 1 and grid[j + 1][i] != "---":
                        print(' ', end='')

                    #if grid[j][i][1] != 1 and j + 1 < x * 2 - 1 and grid[j + 1][i] != "---":
                     #   print(' ', end='')


                # if something else is present
                else:
                    print(grid[j][i], end='')

        print()
    print()


def clear_screen():
    """ Clears the screen to show how the protein folds in a nice way. """

    # sleep a little for animation's sake
    time.sleep(1)

    # clear the terminal window
    os.system("cls")
