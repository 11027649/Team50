# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: score(). A function that returns the score.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from utility.update_grid import update_grid
from protein_class import Amino

def score(protein):
    """ A function that returns a stability score for a specific folding of a
        protein. Does this by taking the global grid, coordinates and protein
        string. . """

    score = 0
    grid = protein.grid
    coordinates = protein.coordinates

    # for all aminos in the protein
    for i in range(protein.length):

        # the coordinates are stored in an array. i is the amino acid that you're
        # looking for, [0] or [1] are x and y
        x = coordinates[i][0]
        y = coordinates[i][1]
        z = coordinates[i][2]


        # initialize the first coordinate independent of direction
        coor1 = grid[x][y][z]

        # if it's an H, do something with the score
        # check only under and to the right to not count interactions double
        if not coor1.letter == "P":
            if type(coor1) == Amino:

                # initialize the second coordinate depending on the direction
                coor2x = grid[x + 1][y][z]
                coor2y = grid[x][y + 1][z]
                coor2z = grid[x][y][z + 1]

                # will check if there is a score between coor1 and coor2
                score -= calc_score(coor1, coor2x)
                score -= calc_score(coor1, coor2y)
                score -= calc_score(coor1, coor2z)

    return score

def calc_score(coor1, coor2):
    if type(coor2) == Amino \
        and not coor2.letter == "P" \
        and abs(coor1.num_id - coor2.num_id) > 1:

        if coor2.letter == coor1.letter:
            if coor2.letter == "C":
                return 5
            else:
                return 1
        else:
            return 1
    return 0
