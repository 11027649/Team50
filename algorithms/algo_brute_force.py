
from utility.score import score


def brute_force(run_info, protein):
    numberArray = []
    length = protein.length
    def recursieveFunctie(value):
        if value == 1:
            for i in range(6):
                numberArray[value - 1] = i
                protein = calc_coords(numberArray)
        else:

            for i in range(6):
                numberArray[value - 1] = i
                recursieveFunctie(value - 1)

    for i in range(1, len - 2):

        numberArray = []
        for j in range (len - 2):
            numberArray.append(0)
        numberArray[i] = 1
        recursieveFunctie(i)


    return [run_info, protein]

def calc_coords(numberArray, protein):
    directions = numberArray
    # get the length
    length = protein.length
    coordinates = protein.coordinates

    grid_width = length * 2 + 1

    #  make the grid
    grid = [[[0 for i in range(grid_width)] for j in range(grid_width)] for k in range(grid_width)]

    # get starting position
    start_pos = 0
    while directions[start_pos] == 0:
        start_pos += 1


    # iterate from the starting position till the end and put new coordinates
    for i in range(start_pos , length ):
        # get the previous coordinates
        previous_x = coordinates[i - 1][0]
        previous_y = coordinates[i - 1][1]
        previous_z = coordinates[i - 1][2]

        # initialize new coords
        coordinates[i] = [previous_x,previous_y, previous_z]

        # make a correction depending on the direction
        if directions[i] == 0:
            coordinates[i][0] = previous_x + 1
        elif directions[i] == 1:
            coordinates[i][0] = previous_x - 1
        elif directions[i] == 2:
            coordinates[i][1] = previous_y + 1
        elif directions[i] == 3:
            coordinates[i][1] = previous_y - 1
        elif directions[i] == 4:
            coordinates[i][2] = previous_z + 1
        elif directions[i] == 5:
            coordinates[i][2] = previous_z - 1


        # set the coordinatesin the midle of the grid
        x_coor = coordinates[i][0]
        y_coor = coordinates[i][1]
        z_coor = coordinates[i][2]

        grid[x_coor][y_coor][z_coor] = protein.aminos[i]
    protein.grid = grid
    protein.coordinates = coordinates

    stability = score(protein)

    # if the score is lower save that particular grid in winning grid
    if stability < best_score:
        protein.winning_grid = copy.deepcopy(protein.grid)
        protein.winning_coordinates = copy.deepcopy(protein.coordinates)
        best_score = stability
        protein.winning_score = best_score

    else:
        protein.grid = copy.deepcopy(protein.winning_grid)
        protein.coordinates = copy.deepcopy(protein.winning_coordinates)

    return protein
