import time
import os
from animation import print_protein

from amino import Amino
from score import score

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
    protein_to_grid()


def fold_protein(amino_number, direction, grid):
    """ Folds the protein. """
    # saves the old grid
    old_grid = grid


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
                    grid = old_grid
                    exit(1)
            protein[i + amino_number].aa_x = x_pos
            protein[i + amino_number].aa_y = y_pos
            protein[i+ amino_number].direction = check_direction
    correct_protein()
    protein_to_grid()
    # makes from the array protein an according grid with proteins in it

def protein_to_grid():
    # saves the x and y value of the grid
    max_x = 0
    max_y = 0

    # gets the needed height and width of the grid
    for i in range(protein_length):
        if protein[i].aa_x > max_x:
            max_x = protein[i].aa_x
        if protein[i].aa_y > max_y:
            max_y = protein[i].aa_y

    # gets the coordinates of the grid
    cur_x = 0
    cur_y = 0
    global grid
    grid = [[' ' for p in range(max_y+1)] for q in range(max_x+1)]

    for i in range(protein_length):
        cur_x = protein[i].aa_x
        cur_y = protein[i].aa_y
        grid[cur_x][cur_y] = protein[i]
    temporary_print(max_x, max_y)


def temporary_print(max_x, max_y):

    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if not grid[j][i] == ' ':
                print (grid[j][i].letter, end ='')
            else:
                print (grid[j][i], end ='')
        print()

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

def main():
    init_protein()


    fold_protein(1, 'L', grid)
    print('fold 1')


    fold_protein(2, 'L', grid)
    print('fold 2', grid)

    fold_protein(3, 'R', grid)
    print('fold 3')


if __name__ == "__main__":
    main()
