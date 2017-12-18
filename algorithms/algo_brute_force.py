
from utility.score import score
from protein_class import Amino

import copy

counter = 0


def brute_force(run_info, protein):

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)
    protein.winning_score = 0

    for i in range (length):
        protein.coordinates[i] = [protein.coordinates[i][0] + length, protein.coordinates[i][1] + length, protein.coordinates[i][2] + length]

    def recursieveFunctie(value, protein):
        global counter
        counter += 1
        # print(counter, iterations)
        printProgressBar(counter, iterations)
        if value == 1:

            for i in range(check):
                numberArray[value - 1] = i
                numberArray.reverse
                calc_coords(list(reversed(numberArray)), protein)
        else:
            for i in range(check):
                numberArray[value - 1] = i
                recursieveFunctie(value - 1, protein)

    # calculate amount of iterations needed to complete the depth first
    iterations = pow(6, length - 2)
    for i in range (length - 2):
        iterations = (int) (iterations - (2 / 3) * pow(6, i + 1))

    numberArray = []

    # determines how many directions need to be checked
    check = 6

    if run_info.dimension == 0:
        check = 4
    elif run_info == 1:
        check = 6

    for i in range(1, length - 2):
        numberArray = []
        for j in range (length - 2):
            numberArray.append(0)
        numberArray[i] = 1
        progres = pow(5, i + 1)
        recursieveFunctie(i, protein)

    return [run_info, protein]

def calc_coords(numberArray, protein):
    directions = numberArray
    # get the length
    length = protein.length
    coordinates = protein.coordinates[:]

    possible = True
    grid_width = length * 2 + 1

    #  make the grid
    grid = [[[0 for i in range(grid_width)] for j in range(grid_width)] for k in range(grid_width)]

    # get starting position
    start_pos = 0
    while directions[start_pos] == 0:
        start_pos += 1

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
        direction  = directions[i - 2]
        # make a correction depending on the direction
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
    protein.grid = copy.deepcopy(grid)
    protein.coordinates = copy.deepcopy(coordinates)
    best_score = protein.winning_score
    stability = score(protein)

    # if the score is lower save that particular grid in winning grid
    if stability < best_score:
        protein.winning_grid = copy.deepcopy(grid)
        protein.winning_coordinates = copy.deepcopy(coordinates)
        best_score = stability
        protein.winning_score = best_score

    return protein
