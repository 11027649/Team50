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
