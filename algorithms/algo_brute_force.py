# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is part of the protein folding program made by Team50.
#
# It contains a dept firce algoritm called brute force.
# By using a list with directions some mirror variations of folds are prevented.
# The direction list is dependent of the user input.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from protein_class import Amino

import copy



def brute_force(run_info, protein):

    # initialize the length
    length = protein.length

    # make the grid with 2 times as high + 1 to prevent out of range problems
    grid_width = length * 2 + 1

    # initialize an empty winning grid with the grid_width
    protein.winning_grid =  [[[0 for i in range(grid_width)] for j in range(grid_width)] for k in range(grid_width)]

    # set the aminos in the grid starting from the middle of the grid
    for i in range (length):
        new_coordinate = [protein.coordinates[i][0] + length, protein.coordinates[i][1] + length, protein.coordinates[i][2] + length]
        protein.coordinates[i] = new_coordinate

    # initialize the winning coordinates and grid
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)
    for i in range (length):
        coordinates = protein.winning_coordinates
        x_coor = coordinates[i][0]
        y_coor = coordinates[i][1]
        z_coor = coordinates[i][2]

        protein.winning_grid[x_coor][y_coor][z_coor] = protein.aminos[i]

    # initialize the direction list which will detirmine how the protein is folded
    direction_list = []

    # determines how many direction_list need to be checked
    check = 6

    # check will become 4 for 2D and 6 for 3D
    if run_info.dimension == 0:
        check = 4
    elif run_info == 1:
        check = 6


    # this function calculates the right folding sequence
    # value keeps track of how much deeper this function can go
    def recursieveFunctie(value, protein):

        # if the value is 1 the last check is needed
        if value == 1:

            # check in the directions dependent of 2d or 3d
            for i in range(check):
                direction_list[0] = i
                direction_list.reverse
                calc_coords(list(reversed(direction_list)), protein)
        else:
            # go recursive in this function and change the direction_list accordingly
            for i in range(check):
                direction_list[value - 1] = i
                recursieveFunctie(value - 1, protein)

    # this function makes a direction_list
    for i in range(1, length - 1):

        # initialize it empty to enable appending
        direction_list = []

        # initialize the list with zeros
        for j in range (length - 1):
            direction_list.append(0)

        # by putting a one the starting position is detirmined
        # and mirror folds are prevented at that spot
        direction_list[i] = 1

        # go recursive with that list
        recursieveFunctie(i, protein)

    return [run_info, protein]

def calc_coords(direction_list, protein):
    # get the length
    length = protein.length
    coordinates = protein.coordinates[:]

    possible = True
    grid_width = length * 2 + 1

    #  make an empty grid to enable putting the aminos one by one
    grid = [[[0 for i in range(grid_width)] for j in range(grid_width)] for k in range(grid_width)]

    # get starting position
    start_pos = 0
    while direction_list[start_pos] == 0:
        start_pos += 1

    # till the starting position no coordinates are changed so aminos can be put at their coordinates
    for i in range(start_pos):

        # set the coordinatesin the midle of the grid
        x_coor = coordinates[i][0]
        y_coor = coordinates[i][1]
        z_coor = coordinates[i][2]
        grid[x_coor][y_coor][z_coor] = protein.aminos[i]


    # iterate from the starting position till the end and put new coordinates
    for i in range(start_pos + 1 , length ):

        # get the previous coordinates
        previous_x = coordinates[i - 1][0]
        previous_y = coordinates[i - 1][1]
        previous_z = coordinates[i - 1][2]

        # initialize new coords
        coordinates[i] = [previous_x,previous_y, previous_z]
        direction  = direction_list[i - 2]

        # make a correction depending on the direction given in direction_list
        if direction == 0:
            coordinates[i][0] = previous_x + 1
        elif direction == 1:
            coordinates[i][0] = previous_x - 1
        elif direction == 2:
            coordinates[i][1] = previous_y + 1
        elif direction == 3:
            coordinates[i][1] = previous_y - 1
        elif direction == 4:
            coordinates[i][2] = previous_z + 1
        elif direction == 5:
            coordinates[i][2] = previous_z - 1

    # put aminos back afther the start pos
    for i in range(start_pos, length):
        # set the coordinatesin the midle of the grid
        x_coor = coordinates[i][0]
        y_coor = coordinates[i][1]
        z_coor = coordinates[i][2]
        if type(grid[x_coor][y_coor][z_coor]) == Amino:
            possible = False
            break
        grid[x_coor][y_coor][z_coor] = protein.aminos[i]

    if possible == False:
        return

    # copy it back to protein to enable use of score function
    protein.grid = copy.deepcopy(grid)
    protein.coordinates = copy.deepcopy(coordinates)

    # calculate score
    best_score = protein.winning_score
    stability = protein.score()

    # if the score is lower save that particular grid in winning grid
    if stability < best_score:
        protein.winning_grid = copy.deepcopy(grid)
        protein.winning_coordinates = copy.deepcopy(coordinates)
        best_score = stability
        protein.winning_score = best_score

    return protein
