# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# contains the brute force algoritm
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def algo_brute_force(protein, grid):
    # initialize the score and depth
    current_score = 0
    winning_score = 0
    depth = len(protein) -2

    # call the recursive function
    recursive_function(depth, protein)



def recursive_function(depth, protein, grid):

    current_score = score(grid, protein)

    if current_score < winning_score:
        winning_score = current_score
        winning coordinates = []
        for i in range(len(protein)):
            coor_x = protein.aa_x
            coor_y = protein.aa_y
            winningcoordinates.append([coor_x, coor_y])

        winning_coordinates = copy.deepcopy(protein)

        print(winning_coordinates)
        print("\n\nBest so far, stability of " + str(winning_score) + ":\n")
        print_protein()

    if (depth < 1):
        return

    fold(depth, "L")
    recursive_function(depth - 1)
    fold(depth, "R")
    recursive_function(depth - 1)
    fold(depth, "R")
    recursive_function(depth - 1)
    fold(depth, "L")
