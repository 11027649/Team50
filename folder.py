# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# contains the function fold_protein()
# contains the function correct_protein()
# contains the function protein_to_grid()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import copy

def fold_protein(amino_number, direction, grid, protein):
    """ Folds the protein at a given amino_number in a given direction.
        Returns a new grid and new protein if the fold is possible.
        Returns the old grid and old protein if the fold is impossible. """

    # saves the old grid
    old_grid = grid

    # make a deepcopy of the protein to make sure the AA values are saved
    old_protein = copy.deepcopy(protein)

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
    for i in range(1, len(protein) - amino_number):
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
                    print("IMPOSSIBLE FOLD: will use old grid")

                    # reset protein to the old protein and return from the function
                    grid_and_protein = [old_grid, old_protein]
                    return grid_and_protein

            protein[i + amino_number].aa_x = x_pos
            protein[i + amino_number].aa_y = y_pos
            protein[i+ amino_number].direction = check_direction
    protein = correct_protein(protein)
    grid = protein_to_grid(protein)

    grid_and_protein = [grid, protein]
    return grid_and_protein


def correct_protein(protein):
    """ Takes the protein and corrects the coordinates. Does this by taking
        100 as a correction factor for the x and y coordinates. The correction
        factor is that high to make sure the min_x and min_y values are lower then
        this factor. """

    min_x = 100
    min_y = 100

    # gets a correction factor for the string (also if it is higher than 0)
    for i in range(len(protein)):

        # when the coordinates in the Amino Acid are lower than min_x
        if protein[i].aa_x < min_x:

            # adjust min_x to the correct value
            min_x = protein[i].aa_x

        # same for the min_y value
        if protein[i].aa_y < min_y:
            min_y = protein[i].aa_y

    # corrects the string
    for i in range(len(protein)):
        protein[i].aa_x += -(min_x)
        protein[i].aa_y += -(min_y)

    return protein

def protein_to_grid(protein):
    """ Takes the protein and works with the coordinates to put the protein
        in a grid. Returns a grid with changes. """

    # saves the x and y value of the grid
    max_x = 0
    max_y = 0

    # iterates over the amino coordinates to find the max coordinates of the grid
    for i in range(len(protein)):

        # if the x coordinate of the amino is higher than max_x
        if protein[i].aa_x > max_x:

            # adjust max_x to the correct value
            max_x = protein[i].aa_x

        # same for the y coordinate
        if protein[i].aa_y > max_y:
            max_y = protein[i].aa_y

    # gets the coordinates of the grid
    cur_x = 0
    cur_y = 0

    # initializes the grid for this file
    grid = [[' ' for p in range(max_y + 1)] for q in range(max_x + 1)]

    # puts the Amino class instances in the grid
    for i in range(len(protein)):
        cur_x = protein[i].aa_x
        cur_y = protein[i].aa_y
        grid[cur_x][cur_y] = protein[i]

    return grid