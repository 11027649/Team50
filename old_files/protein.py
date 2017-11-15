import time
import os
from colorama import init
init()

protein = []
protein_length = 0

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
    if protein_length > 10:
        print("Protein too large...")
        exit(1)

    # check if only P and H amino acids are given
    for letter in protein_string:
        if (letter.upper() != 'P' and letter.upper() != 'H'):
            print("Please only insert P's and H's...")
            exit(1)

    # set all directions of the amino acids to Continue, en if it's the last one, to End
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

    # starts at -1 to makes sure the starting position is 0
    # lol whut?
    x_pos = 0
    y_pos = 0

    # 1(right) 2(down) 3(left) 0(up), standard direction is to the right
    direction = 1

    # for each amino acid in the protein
    for i in range(protein_length):

        # gets the right direction
        if protein[i].pos_next == 'L':
            direction -= 1
        if protein[i].pos_next == 'R':
            direction += 1

        # makes sure the direction is the right format (never above 3)
        # do we really need to do this, as we will be inputting the directions ourselves?
        direction %= 4;

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
            min_y = -y_pos
        if x_pos < min_x:
            min_x = -x_pos

        # append the amino acids and its coordinates on the grid
        coordinates.append([x_pos, y_pos, protein[i]])
    x = min_x + max_x + 1
    y = min_y + max_y + 1

    # initialize the grid
    grid = [[' ' for p in range(y)] for q in range(x)]
    for i in range(protein_length):

        coor_x = coordinates[i][0] + min_x
        coor_y = coordinates[i][1] + min_y

        grid[coor_x][coor_y] = coordinates[i][2]

    # print the grid
    for i in range(y):

        # print rows
        for j in range(x):

            # if grid is nothing, print space
            if grid[j][i] == ' ':
                print(" ", end='')

            # else print amino acid letter
            else:
                # print H blue
                if grid[j][i].letter == 'H':
                    print('\033[34;1m' + grid[j][i].letter, end='')
                    print('\033[0m', end= '')

                # print P red
                elif grid[j][i].letter == 'P':
                    print('\033[31;1m' + grid[j][i].letter, end='')
                    print('\033[0m', end= '')

            print("   ", end='')

        print()
        print()

    print()

def clear_screen():
    """ Clears the screen to show how the protein folds in a nice way. """

    # sleep a little for animation's sake
    time.sleep(1)

    # clear the terminal window, clear in IDE, cls in Windows
    os.system("cls")

## DIT IS DE MAIN ##
clear_screen()

init_protein()
clear_screen()

print_protein()
clear_screen()

fold_protein(2, 'L')
print_protein()
clear_screen()

fold_protein(5, 'L')
print_protein()
clear_screen()

fold_protein(8, 'R')
print_protein()
clear_screen()