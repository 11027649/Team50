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
            protein.append(Amino(protein_string[i].upper(), 'E', i, 0, 1))
        else:
            protein.append(Amino(protein_string[i].upper(), 'C', i, 0, 1))


def fold_protein(amino_number, direction):
    """ Folds the protein. """

    # check if valid folding input
    if direction != 'L' and direction != 'R':
        print("This ain't no valid foldin' input dude.")
        exit(1)

    # we need to check here if not 2 amino acids are on the same point in the grid (pseudocode)
    # x_start = protein[amino_number].aa_x
    # y_start = protein[amino_number].aa_y
    # check_direction = protein[amino_number].direction
    # for i in range(protein_length - amino_number):
    #     if check_direction == 0:
    #         y_pos += 1
    #     elif check_direction == 1:
    #         x_pos += 1
    #     elif check_direction == 2:
    #         y_pos -= 1
    #     elif check_direction == 3:
    #         x_pos -= 1

    # if not, write direction into amino acid
    protein[amino_number].pos_next = direction
    # afther an amino acid is formed it has to make the grid to get the coordinates
    make_grid()

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
    new_direction = 1

    # for each amino acid in the protein
    for i in range(protein_length):

        # gets the coordinates of this amino acid
        if new_direction == 0:
            y_pos += 1
        elif new_direction == 1:
            x_pos += 1
        elif new_direction == 2:
            y_pos -= 1
        elif new_direction == 3:
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
            new_direction -= 1
        if protein[i].pos_next == 'R':
            new_direction += 1

        # makes sure the direction is the right format (never above 3)
        new_direction %= 4;

        # gives protein an x and y value, however these are temporary
        # the x and y value will be set to the correct value later
        # for the x value the lowest x value has to be added (same for y)
        protein[i].aa_x = x_pos
        protein[i].aa_y = y_pos
        protein[i].direction = new_direction
    # makes sure the right coordinates are given(here the lowest x value is added)
    for i in range(len(protein)):
        protein[i].aa_x = protein[i].aa_x + min_x
        protein[i].aa_y = protein[i].aa_y + min_y


def main():
    init_protein()
    make_grid()
    fold_protein(2, 'L')
    fold_protein(4, 'L')
    make_grid()

    # print_protein(x,y, protein_length)
    # initialize_grid(x, y, protein_length, aa_info)
    # print_protein()
    # fold_protein(2, 'L')
    # initialize_grid(min_x, min_y)
    # visualize_fold(min_x, min_y, x, y, aa_info)


if __name__ == "__main__":
    main()
