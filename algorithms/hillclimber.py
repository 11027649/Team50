# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is part of the protein folding program made by Team50.
#
# It contains three variations of a Hill Climber algorithm.
# For the "normal" version, you can change the boolean accept to force the
# the algorithm to do 14 folds that are accepted.
# Here, you can change the amount of iterations by changing iterations.
# You can change the amount of folds per iterations by changing folds.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #2

from visualization.progress_bar import printProgressBar

from random import randint
import copy
import csv

def hillclimber(run_info, protein):
    """ This is an algorithm that does 14 random folds per iteration. You can
        force the algorithm to do 14 folds that are accepted by changing the accept
        boolean to False. After the 14 folds it checks whether the protein is more
        stable then before. If so, the changes are kept, else the old protein is
        restored. This continues for n iterations. """

    # store algorithm in file, write a header
    run_info.algorithm = "Hill Climber"
    run_info.generate_filepath("hc_")
    run_info.generate_header(protein.protein_string)

    # will keep track of the score
    best_score = 0

    # determines how many iterations are needed
    iterations = 5000

    # determines the amount of folds this hillclimber will do
    folds = 14

    accept = True
    length = protein.length

    # make sure winning_grid and winning_coordinates are not empty
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    # store data in .csv
    with open(run_info.filepath, 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

            # print progressbar
            printProgressBar(i, iterations)
            datawriter.writerow([i] + [best_score])

            # do random folds
            for j in range(folds):
                random_value = get_random_value(run_info.dimension, protein.length - 2)

                if accept == True:
                    returncode_and_protein = protein.fold(random_value[0], random_value[1])
                    protein = returncode_and_protein[1]

                # if you set accept to false, you'll force n folds that are possible
                # this is not better, but we left it in here because you should be able
                # to generate the same results
                else:
                    returncode_and_protein = protein.fold(random_value[0], random_value[1])

                    while returncode_and_protein[0] == "collision":
                        random_value = get_random_value(run_info.dimension, protein.length - 2)
                        returncode_and_protein = protein.fold(random_value[0], random_value[1])
                    protein = returncode_and_protein[1]

            # calculate the score
            stability = protein.score()

            # if the score is lower save that particular grid in winning grid
            if stability < best_score:
                protein.winning_grid = copy.deepcopy(protein.grid)
                protein.winning_coordinates = copy.deepcopy(protein.coordinates)
                protein.winning_score = best_score = stability

            else:
                protein.grid = copy.deepcopy(protein.winning_grid)
                protein.coordinates = copy.deepcopy(protein.winning_coordinates)

    return [run_info, protein]


def fold_control_hillclimber(run_info, protein):
    """ This is an algorithm that is a variation at the normal hillclimber.
        It does 14 random folds per iteration. The folds must be possible here,
        because after every fold the score is checked. If it's higher we keep that
        protein. Else the old protein is restored. This continues for n iterations. """

    # store algorithm in file, write a header
    run_info.algorithm = "Hill Climber (with fold control)"
    run_info.generate_filepath("hc_fc_")
    run_info.generate_header(protein.protein_string)

    # will keep track of the score
    best_score = 0

    # determines how many iterations are needed
    iterations = 5000

    # determines the amount of folds this hillclimber will do
    folds = 14

    length = protein.length

    # prevent winning_grid and winning_coordinates from being empty
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    # store data in .csv
    with open(run_info.filepath, 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

            # print the progressbar
            printProgressBar(i, iterations)
            datawriter.writerow([i] + [best_score])

            # do random folds
            for j in range(folds):

                # initial fold
                random_value = get_random_value(run_info.dimension, protein.length - 2)
                returncode_and_protein = protein.fold(random_value[0], random_value[1])

                # force a fold that is possible, and control if this is a better fold
                while returncode_and_protein[0] == "collision":
                    random_value = get_random_value(run_info.dimension, protein.length - 2)
                    returncode_and_protein = protein.fold(random_value[0], random_value[1])

                stability = protein.score()

                # if the score is lower save that particular grid in winning grid
                # and stop with folding this iteration
                if stability < best_score:
                    protein.winning_grid = copy.deepcopy(protein.grid)
                    protein.winning_coordinates = copy.deepcopy(protein.coordinates)
                    protein.winning_score = best_score = stability
                    break

            # set the winning grid back as current grid
            protein.grid = copy.deepcopy(protein.winning_grid)
            protein.coordinates = copy.deepcopy(protein.winning_coordinates)

    return [run_info, protein]


def extend_fold_hillclimber(run_info, protein):
    """ This is an algorithm that is a variation at the normal hillclimber.
        It does 2 random folds per iteration. The folds do not have to be possible.
        If for 1000 iterations no better score is found, the fold amount is increased
        by 1, and thus will become 3. It tries again finding a better score, and this
        progress goes on and on, untill no better solution can be found for up to 100 folds
        per iteration."""

    # store algorithm in file, write a header
    run_info.algorithm = "Extend Fold Hill Climber"
    run_info.generate_filepath("hc_ef_")
    run_info.generate_header(protein.protein_string)

    # will keep track of the score
    best_score = 0

    # max amount of iterations of we will try for each fold amount
    iterations = 30

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    # store data in .csv
    with open(run_info.filepath, 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

            # extend starts with 2, becomes bigger every time, set counter
            extend = 2
            counter = 0
            found = False

            # determines the end of the progressbar
            end_extend = 101

            # while no better score is found
            while found == False:

                # fold "extend" times
                for j in range(extend):
                    printProgressBar(extend, end_extend)
                    datawriter.writerow([i] + [best_score])

                    random_value = get_random_value(run_info.dimension, protein.length - 2)

                    # do a valid fold
                    returncode_and_protein = protein.fold(random_value[0], random_value[1])
                    protein = returncode_and_protein[1]

                    # if the score is lower save that particular grid in winning grid
                    stability = protein.score()

                    # if stability is lower, save this last grid anc break
                    if stability < best_score:
                        protein.winning_grid = copy.deepcopy(protein.grid)
                        protein.winning_coordinates = copy.deepcopy(protein.coordinates)
                        best_score = protein.winning_score = stability
                        found = True
                        break

                    counter += 1

                    # if 1000 non-improving counts were counted, extend the fold amount
                    if counter > 1000:
                        extend += 1
                        counter = 0

                    # if extend is larger then 100 though, stop the algorithm
                    if extend > 100:
                        return [run_info, protein]


def get_random_value(dimension, length):
    """ This is a function that returns an array with a random aminonumber and
        direction, to make random folds. Also used in Simulated Annealing. """

    # get a random integer between one and length
    aminonumber = randint(1, length)

    # if 2D is chosen
    if (dimension == 0):
        value = randint(0,1)

    # if 3D is chosen
    if (dimension == 1):
        value = randint(0,3)

    # change fram a value to a direction
    if value == 0:
        direction = "L"
    elif value == 1:
        direction = "R"
    elif value == 2:
        direction = "U"
    else:
        direction = "D"

    # return the random amino and fold-direction
    return [aminonumber, direction]
