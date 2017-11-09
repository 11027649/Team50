import time
import os
from animation import print_protein
from amino import Amino

from colorama import init
init()


# set up variables
protein = []
protein_length = 0
ALLOWED_LENGTH = 20
min_x = 0
min_y = 0
x = 0
y = 0

aa_info = []

def init_protein():
    """ Gets an input from the user and makes it usable to fold.
        Initializes all the aminos: Letter, Next position, and coordinates. """

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
    # give the protein coordinates: y = 0 and x = 0 + i
    for i in range(protein_length):
        if i == protein_length - 1:
            protein.append(Amino(protein_string[i].upper(), 'E', i, 0))
        else:
            protein.append(Amino(protein_string[i].upper(), 'C', i, 0))


def fold_protein(amino_number, direction):
    """ Folds the protein. """

    # check if valid folding input
    if direction != 'L' and direction != 'R':
        print("This ain't no valid foldin' input dude.")
        exit(1)

    # we need to check here if not 2 amino acids are on the same point in the grid

    # if not, write direction into amino acid
    protein[amino_number].pos_next = direction


def make_grid():

    # initialize coordinates
    max_x = 0
    max_y = 0
    min_y = 0
    min_x = 0
    # starts at 0 to makes sure the starting position is 0
    x_pos = 0
    y_pos = 0

    # 1(right) 2(down) 3(left) 0(up), standard direction is to the right
    direction = 1

    print('Hallo ik ben in make_grid aangekomen')
    print(protein_length)

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
        print(protein[i].letter)

        protein[i].aa_x = x_pos
        protein[i].aa_y = y_pos

        aa_info.append([x_pos, y_pos, protein[i].letter, direction])

    global x
    x = min_x + max_x + 1
    global y
    y = abs(min_y) + max_y + 1

    # makes sure the right coordinates are given
    for i in range(len(aa_info)):
        aa_info[i] = [x_pos + min_x, y_pos + min_y, protein[i].letter, direction]


def main():
    init_protein()
    make_grid()

    print_protein(x,y, protein_length)

    fold_protein(3, 'L')
    initialize_grid(x, y, protein_length, aa_info)
    print_protein()

    # fold_protein(2, 'L')
    # initialize_grid(min_x, min_y)
    # visualize_fold(min_x, min_y, x, y, aa_info)


if __name__ == "__main__":
    main()
