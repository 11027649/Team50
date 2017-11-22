# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# contains the function init_protein
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from folder import protein_to_grid
from amino import Amino

def init_protein():
    """ Gets an input from the user and makes it usable to fold.
        Initializes all the aminos: Letter, Next position, and coordinates. """

    ALLOWED_LENGTH = 20
    protein = []

    # ask user for protein string as input, max length
    protein_string = input("Insert protein string: ")

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
    grid = protein_to_grid(protein)

    grid_and_protein = [grid, protein]
    return grid_and_protein