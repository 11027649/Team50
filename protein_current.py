import time
import os
from colorama import init
init()

# set up variables
protein = []
protein_length = 0
ALLOWED_LENGTH = 20

# save position of each amino acid to remember which ones are linked
class Amino():
    def __init__(self, letter, pos_next):
        self.letter = letter
        self.pos_next = pos_next


def init_protein():
    """ Gets an input from the user and makes it usable to fold. """

    # ask user for protein string as input, max length
    protein_string = input("Insert protein string: ")
    global protein_length
    protein_length = len(protein_string)

    # check if protein isn't too long
    if protein_length > ALLOWED_LENGTH:
        print("Protein too large...")
        exit(1)

    # check if only P and H amino acids are given
    for letter in protein_string:
        if (letter.upper() != 'P' and letter.upper() != 'H'):
            print("Please only insert P's and H's...")
            exit(1)

    # set all directions of the amino acids to Continue, and if it's the last one, to End
    for i in range(protein_length):
        if i == protein_length - 1:
            protein.append(Amino(protein_string[i].upper(), 'E'))
        else:
            protein.append(Amino(protein_string[i].upper(), 'C'))


def fold_protein(amino_number, direction):
    """ Folds the protein. """

    # check if valid folding input
    if direction != 'L' and direction != 'R':
        print("This ain't no valid foldin' input dude.")
        exit(1)

    # we need to check here if not 2 amino acids are on the same point in the grid

    # if not, write direction into amino acid
    protein[amino_number].pos_next = direction


def print_protein():
    """ Prints the protein in a nice way. """

    # make array for coordinates
    coordinates = []

    # initialize coordinates
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    # starts at 0 to makes sure the starting position is 0
    x_pos = 0
    y_pos = 0

    # 1(right) 2(down) 3(left) 0(up), standard direction is to the right
    direction = 1

    # for each amino acid in the protein
    for i in range(protein_length):

        # gets the coordinates of this amino acid
        if direction == 0:
            y_pos -= 1
        elif direction == 1:
            x_pos += 1
        elif direction == 2:
            y_pos += 1
        elif direction == 3:
            x_pos -= 1

        # save the highest and lowest coordinates for making the grid
        if y_pos > max_y:
            max_y = y_pos
        if x_pos > max_x:
            max_x = x_pos

        if y_pos < min_y:
            min_y = -abs(y_pos)
        if x_pos < min_x:
            min_x = -x_pos

        # gets the right direction
        if protein[i].pos_next == 'L':
            direction -= 1
        if protein[i].pos_next == 'R':
            direction += 1
        # makes sure the direction is the right format (never above 3)
        direction %= 4;

        # append the amino acids and its coordinates on the grid
        coordinates.append([x_pos, y_pos, protein[i].letter, direction])

    # gets a whitespace between the inserted protein and the print
    print()

    x = min_x + max_x + 1
    y = abs(min_y) + max_y + 1

    # initialize the grid
    grid = [['  ' for p in range(y * 2 - 1)] for q in range(x * 2 - 1)]
    for i in range(protein_length):

        coor_x = (coordinates[i][0] + min_x) * 2
        coor_y = (coordinates[i][1] + abs(min_y)) * 2


        grid[coor_x][coor_y] = [coordinates[i][2], coordinates[i][3]]

    # add layout, making the grid 2* as big, to add bonds
        # makes sure the last protein does not print its extra layout
        if i != protein_length - 1:
            if coordinates[i][3] == 0:
                grid[coor_x][coor_y - 1] = '|'
            elif coordinates[i][3] == 1:
                grid[coor_x + 1][coor_y] = '---'
            elif coordinates[i][3] == 2:
                grid[coor_x][coor_y + 1] = '|'
            elif coordinates[i][3] == 3:
                grid[coor_x - 1][coor_y] = '---'

    # print the grid
    for i in range(y * 2 - 1):

        # print rows
        for j in range(x * 2 - 1):

                # Hoi dit is een comment
                # print H blue
                if grid[j][i][0] == 'H':
                    print('\033[34;1m' + grid[j][i][0], end='')
                    print('\033[0m', end='')


                # print P red
                elif grid[j][i][0] == 'P':
                    print('\033[31;1m' + grid[j][i][0], end='')
                    print('\033[0m', end='')
                    
                    if grid[j][i][1] != 1 and j + 1 < x * 2 - 1 and grid[j + 1][i] != "---":
                        print(' ', end='')


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

## DIT IS DE MAIN ##
init_protein()


fold_protein(1, 'L')
fold_protein(2, 'L')
fold_protein(3, 'R')
fold_protein(4, 'R')
fold_protein(6, 'R')
fold_protein(9, 'R')
fold_protein(12, 'R')
fold_protein(16, 'R')


print_protein()

# phpphpphpphpphpphpp
