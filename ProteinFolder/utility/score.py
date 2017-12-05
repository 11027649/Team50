# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: score(). A function that returns the score.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from utility.update_grid import update_grid
from global_vars import amino

import global_vars
global_vars.init()

def score():
    """ A function that returns a stability score for a specific folding of a
        protein. Does this by taking the global grid, coordinates and protein
        string. . """

    score = 0
    grid = global_vars.grid
    coordinates = global_vars.coordinates
    width = len(grid)
    height = len(grid[0])

    # for all aminos in the protein
    for i in range(len(global_vars.protein_string)):

        # the coordinates are stored in an array. i is the amino acid that you're
        # looking for, [0] or [1] are x and y
        x = coordinates[i][0]
        y = coordinates[i][1]

        # save the current id of the amino acid
        cur_id = grid[x][y].num_id

        # if it's an H, do something with the score
        # check only under and to the right to not count interactions double
        if grid[x][y].letter == "H" or "C":

            # check 4 things for right:
                # if it's not the first column (for out of range purposes)
                # if there's an Amino class object on the gridpoint on the left
                # if that class object's letter is an "H"
                # if the two are not "bonded" by checking id's
            if type(grid[x + 1][y]) == amino \
                and not grid[x + 1][y].letter == "P" \
                and abs(cur_id - grid[x + 1][y].num_id) > 1:

                if grid[x][y].letter == grid[x + 1][y].letter:
                    if grid[x][y].letter == "C":
                        score -= 5
                    else:
                        score -= 1


            # same for under
            if type(grid[x][y + 1]) == amino \
                and not grid[x][y + 1].letter == "P" \
                and abs(cur_id - grid[x][y + 1].num_id) > 1:

                if grid[x][y].letter == grid[x][y + 1].letter:
                    if grid[x][y].letter == "C":
                        score -= 5
                    else:
                        score -= 1

    return score