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