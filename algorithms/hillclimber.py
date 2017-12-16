from utility.score import score
from utility.fold import fold

from algorithms.progress_bar import printProgressBar

from random import randint
import copy
import csv


def hillclimber(run_info, protein):
    # if accept is True, folds that collide will count
    # if False only folds that pass will happen
    accept = True

    # will keep track of the score
    best_score = 0

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    iterations = 5000

    run_info.algorithm = "Hill Climber"
    run_info.generate_filepath("hc_")
    run_info.generate_header(protein.protein_string)

    # store data in .csv
    with open(run_info.filepath, 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

            printProgressBar(i, iterations)
            datawriter.writerow([i] + [best_score])

            for j in range(6):
                random_value = get_random_value(run_info.dimension, protein.length - 2)
                if accept == True:
                    returncode_and_protein = fold(random_value[0], random_value[1], protein)
                    protein = returncode_and_protein[1]
                else:
                    returncode_and_protein = fold(random_value[0], random_value[1], protein)

                    while returncode_and_protein[0] == "collision":
                        random_value = get_random_value(run_info.dimension, protein.length - 2)
                        returncode_and_protein = fold(random_value[0], random_value[1], protein)
                    protein = returncode_and_protein[1]

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

    return [run_info, protein]


def fold_control_hillclimber(run_info, protein):
    """ Hillclimber which selects the best out of 14. """

    # will keep track of the score
    best_score = 0

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    iterations = 5000

    run_info.algorithm = "Hill Climber (with fold control)"
    run_info.generate_filepath("hc_fc_")
    run_info.generate_header(protein.protein_string)

    # store data in .csv
    with open(run_info.filepath, 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

            printProgressBar(i, iterations)
            datawriter.writerow([i] + [best_score])

            for j in range(14):
                random_value = get_random_value(run_info.dimension, protein.length - 2)

                returncode_and_protein = fold(random_value[0], random_value[1], protein)
                protein = returncode_and_protein[1]

                stability = score(protein)

                # if the score is lower save that particular grid in winning grid
                if stability < best_score:
                    protein.winning_grid = copy.deepcopy(protein.grid)
                    protein.winning_coordinates = copy.deepcopy(protein.coordinates)
                    best_score = stability
                    protein.winning_score = best_score

                    break

            # set the winning grid back as current grid
            protein.grid = copy.deepcopy(protein.winning_grid)
            protein.coordinates = copy.deepcopy(protein.winning_coordinates)

    return [run_info, protein]


def extend_fold_hillclimber(run_info, protein):

    run_info.algorithm = "Extend Fold Hill Climber"
    run_info.generate_filepath("hc_ef_")
    run_info.generate_header(protein.protein_string)

    # will keep track of the score
    best_score = 0

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    iterations = 30

    # store data in .csv
    with open(run_info.filepath, 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

            extend = 2
            counter = 0
            found = False

            while found == False:

                for j in range(extend):
                    print(j, extend)

                    printProgressBar(extend, 101)
                    datawriter.writerow([i] + [best_score])

                    random_value = get_random_value(run_info.dimension, protein.length - 2)

                    # do a valid fold
                    returncode_and_protein = fold(random_value[0], random_value[1], protein)
                    protein = returncode_and_protein[1]

                    # if the score is lower save that particular grid in winning grid

                    stability = score(protein)

                    if stability < best_score:
                        protein.winning_grid = copy.deepcopy(protein.grid)
                        protein.winning_coordinates = copy.deepcopy(protein.coordinates)
                        best_score = stability
                        protein.winning_score = best_score

                        found = True

                        break

                    counter += 1

                    if counter > 1000:
                        extend += 1
                        counter = 0

                    if extend > 100:
                        return [run_info, protein]


def get_random_value(dimension, length):
    """ This is a function that returns an array with a random direction and
        aminonumber, to make random folds. Also used in Simulated Annealing. """

    aminonumber = randint(1, length)
    direction = ""
    value = 6
    # if 2D is chosen
    if (dimension == 0):
        value = randint(0,1)
    # if 3D is chosen
    if (dimension == 1):
        value = randint(0,3)
    if value == 0:
        direction = "L"
    elif value == 1:
        direction = "R"
    elif value == 2:
        direction = "U"
    else:
        direction = "D"
    return [aminonumber, direction]
