# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# contains the main function
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from folder import fold_protein
from initialize import init_protein
from animation import visualize_protein
from amino import Amino
from score import score
from helper_prints import print_protein, print_coordinates
from queue import Queue

def main():
    """ In the main function the alogrithm will be implemented. """

    # initialize
    grid_and_protein = []
    grid_and_protein = init_protein()

    for bond in range(1, len(protein) - 1):
        if protein[bond].pos_next == 'C':
            print(bond, end ='**')
            print()
            grid_and_protein = fold_protein(bond, 'R', grid, protein)
            grid = grid_and_protein[0]
            protein = grid_and_protein[1]
            print_protein(grid)
            stability = score(grid, protein)
            print("The stability of this protein is: " + str(stability))





if __name__ == "__main__":
    main()
