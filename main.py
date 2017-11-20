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

    # a first in first out open set
    open_set = Queue()

    # an empty set to maintain visited nodes
    closed_set = set()

    # initialize
    grid_and_protein = []
    grid_and_protein = init_protein()

    grid = grid_and_protein[0]
    protein = grid_and_protein[1]

    open_set.put(grid)

    # queue.empty returns true if queue is empty
    while not open_set.empty():
        parent_grid = open_set.get()

        # add current state to closed_set
        closed_set.update(parent_grid) 

        for bond in range(1, len(protein) - 1):
            if protein[bond].pos_next == 'C':
                print(str(bond) + "**")

                child_state = fold_protein(bond, 'R', grid, protein)
                grid = child_state[0]
                protein = child_state[1]
                print_protein(grid)
                stability = score(grid, protein)
                print("The stability of this protein is: " + str(stability))

                # if this child is in closed_set
                if grid in closed_set:
                    
                    # don't make anymore children
                    continue

                # if not in closed_set
                if grid not in closed_set:

                    # go and make children
                    open_set.put(grid)                  

if __name__ == "__main__":
    main()