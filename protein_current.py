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
    # gives each amino an ID to see easily if the amino's are bonded or not
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

    # if not, write direction into amino acid
    protein[amino_number].pos_next = direction
    if direction == 'L':
        check_direction = protein[amino_number].direction - 1
    if direction == 'R':
        check_direction = protein[amino_number].direction + 1
    check_direction %= 4
    protein[amino_number].direction = check_direction

    # we need to check here if not 2 amino acids are on the same point in the grid (pseudocode)
    x_pos = protein[amino_number].aa_x
    y_pos = protein[amino_number].aa_y

    # iterates over protein and checks if the coordinates already exist
    for i in range(1, protein_length - amino_number):
        protein[i + amino_number]


        # gives new coordinates
        if check_direction == 0:
             y_pos += 1
        elif check_direction == 1:
            x_pos += 1
        elif check_direction == 2:
            y_pos -= 1
        elif check_direction == 3:
            x_pos -= 1
        # gets the right direction
        if protein[i + amino_number].pos_next == 'L':
            check_direction -= 1
        if protein[i + amino_number].pos_next == 'R':
            check_direction += 1
        check_direction %= 4
        # checks if the coordinates already exist

        for j in range(i + amino_number - 1):
            if protein[j].aa_x == x_pos:
                if protein[j].aa_y == y_pos:
                    print("yeah this fold is not possible")
                    exit(1)
            protein[i + amino_number].aa_x = x_pos
            protein[i + amino_number].aa_y = y_pos
            protein[i+ amino_number].direction = check_direction
    correct_protein()


def correct_protein():
    # needed for a correction factor (100 to make sure the x and y coordinates
    # will be lower than this factor)
    min_x = 100
    min_y = 100
    # gets a correction factor for the string (also if it is higher than 0)
    for i in range(len(protein)):
        if protein[i].aa_x < min_x:
            min_x = protein[i].aa_x
        if protein[i].aa_y < min_y:
            min_y = protein[i].aa_y
    for i in range(len(protein)):
        protein[i].aa_x += -(min_x)
        protein[i].aa_y += -(min_y)
    print(min_x, end = 'min_x')

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

def print_coordintes():
    for i in range(len(protein)):
        print(protein[i].aa_x, end ='<x>')
        print(protein[i].aa_y, end ='<y>')
        print(protein[i].direction, end ='<direction>')
        print()


def main():
    init_protein()

    fold_protein(1, 'L')
    print('fold 1')
    print_coordintes()

    print()
    fold_protein(2, 'L')
    print('fold 2')
    print_coordintes()
    print()
    fold_protein(3, 'R')
    print('fold 3')
    print_coordintes()
    print()
    make_grid()



if __name__ == "__main__":
    main()
