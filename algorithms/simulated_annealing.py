# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is part of the protein folding program made by Team50.
#
# It contains three variations of a Simulated Annealing algorithm.
# You can change the amount of iterations by changing N. 
# You can change the begin temperature by changing T0 = Ti = x, where x is the
# temperature you want.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from algorithms.hillclimber import get_random_value
from visualization.progress_bar import printProgressBar

from random import randint
import copy
import csv
import math


def simulated_annealing(run_info, protein):
    """ This is an algorithm that does 14 random folds per iteration. The system 
        cools from 1 degree Celsius to 0 degrees, at a linear rate. The hotter it 
        is, the easier detoriations are accepted. When the detoriation is bigger, 
        it is also less likely to be accepted. There's an extra so-called adapt 
        grid to make sure the winning grid contains the most stable protein. """

    length = protein.length
    protein.winning_grid = adapt_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = adapt_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 5000
    T0 = Ti = 1
    Tn = 0
    current_score = 0

    folds = 14
    adapt_score = 0

    # store algorithm in file, write a header
    run_info.algorithm = "Simulated Annealing"
    run_info.generate_filepath("sa_")
    run_info.generate_header(protein.protein_string)

    # store data in .csv
    with open(run_info.filepath, 'w', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do N times 10 random folds and keep track of the best value
        for i in range(N):

            printProgressBar(i, N)
            datawriter.writerow([i] + [current_score])

            # do random folds
            for j in range(folds):
                random_value = get_random_value(run_info.dimension, protein.length - 2)
                returncode_and_protein = protein.fold(random_value[0], random_value[1])
                protein = returncode_and_protein[1]

            old_score = current_score
            # calculate stability of the protein
            current_score = protein.score()

            # if the score is lower save that particular grid in winning grid
            if current_score < protein.winning_score:
                protein.winning_grid = adapt_grid = copy.deepcopy(protein.grid)
                protein.winning_coordinates = adapt_coordinates =  copy.deepcopy(protein.coordinates)

                # update winning_score
                protein.winning_score = adapt_score = current_score

            # if the score is higher, calculate acceptance chance
            else:
                # calculate acceptance chance
                difference = protein.winning_score - current_score
                acceptance_chance = math.exp(difference / Ti)

                # generate random compare value
                value = randint(1,10000)/10000

                # if acceptance_chance < value, the deterioration is not accepted
                if acceptance_chance < value:

                    # if not accepted, restore the old grid
                    protein.grid = copy.deepcopy(adapt_grid)
                    protein.coordinates = copy.deepcopy(adapt_coordinates)
                    current_score = adapt_score

                # if accepted
                else:
                    # update changes anyway in the grid
                    adapt_grid = copy.deepcopy(protein.grid)
                    adapt_coordinates = copy.deepcopy(protein.coordinates)

            # cool system linear
            Ti = T0 - (i * (T0 - Tn) / N)

    return [run_info, protein]


def simulated_annealing_control(run_info, protein):
    """ This is an algorithm that is almost the same as the "normal" simulated
        annealing. The difference is that, here, every fold out of the 14 we do
        is checked and accepted if it's a better score. If a better score is found,
        the boolean found_better becomes True, so we can skip the calculate
        acceptance chance part for that iteration. """

    length = protein.length
    protein.winning_grid = adapt_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = adapt_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 5000
    T0 = Ti = 1
    Tn = 0
    current_score = 0

    folds = 14

    adapt_score = 0


    run_info.algorithm = "Simulated Annealing (with fold control)"
    run_info.generate_filepath("sa_fc_")
    run_info.generate_header(protein.protein_string)

    # store data in .csv
    with open(run_info.filepath, 'w', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do N times 14 random folds and keep track of the best value
        for i in range(N):

            printProgressBar(i, N)
            datawriter.writerow([i] + [current_score])

            # this variable checks if a better score is found in 14 folds
            found_better = False
            old_score = current_score

            # do .. random folds and check each fold for a better score
            for j in range(folds):
                # initial random value
                random_value = get_random_value(run_info.dimension, protein.length - 2)
                returncode_and_protein = protein.fold(random_value[0], random_value[1])

                while returncode_and_protein[0] == "collision":
                    random_value = get_random_value(run_info.dimension, protein.length - 2)
                    returncode_and_protein = protein.fold(random_value[0], random_value[1])
                protein = returncode_and_protein[1]

                # calculate stability of the protein
                current_score = protein.score()

                # if the score is lower save that particular grid in winning grid
                if current_score < protein.winning_score:
                    protein.winning_grid = adapt_grid = copy.deepcopy(protein.grid)
                    protein.winning_coordinates = adapt_coordinates =  copy.deepcopy(protein.coordinates)

                    # update winning_score
                    protein.winning_score = adapt_score = current_score
                    found_better = True

                    break


            if found_better == False:
                # calculate acceptance chance
                difference = protein.winning_score - current_score
                acceptance_chance = math.exp(difference / Ti)

                # generate random compare value
                value = randint(1,10000)/10000

                # if acceptance_chance <= value, the deterioration is not accepted
                if acceptance_chance < value:

                    # if not accepted, restore the old grid
                    protein.grid = copy.deepcopy(adapt_grid)
                    protein.coordinates = copy.deepcopy(adapt_coordinates)
                    current_score = adapt_score

                # if accepted
                else:
                    # update changes anyway in the grid
                    adapt_grid = copy.deepcopy(protein.grid)
                    adapt_coordinates = copy.deepcopy(protein.coordinates)



        # cool system linear
        Ti = T0 - (i * (T0 - Tn) / N)

    return [run_info, protein]


def simulated_annealing_reheat(run_info, protein):
    """ This is an algorithm that is also a variation at the normal algorithm.
        In this algorithm the environment is reheated to 1 degree at half of the
        iterations. This way, the algorithm can escape from a local minimum (in some
        cases, not in all...) """

    length = protein.length
    protein.winning_grid = adapt_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = adapt_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 10000
    T0 = Ti = 1
    Tn = 0
    current_score = 0

    minus = 0
    folds = 14

    # store algorithm in file, write a header
    run_info.algorithm = "Simulated Annealing (with reheat)"
    run_info.generate_filepath("sa_wr_")
    run_info.generate_header(protein.protein_string)

    # store data in .csv
    with open(run_info.filepath, 'w', newline='') as datafile:
        datawriter = csv.writer(datafile)

        # do N times 10 random folds and keep track of the best value
        for i in range(N):

            if i == (N / 2):
                minus = N / 2

            printProgressBar(i, N)
            datawriter.writerow([i] + [current_score])

            # do random folds
            for j in range(folds):
                random_value = get_random_value(run_info.dimension, protein.length - 2)
                returncode_and_protein = protein.fold(random_value[0], random_value[1])
                protein = returncode_and_protein[1]

            old_score = current_score

            # calculate stability of the protein
            current_score = protein.score()

            # if the score is lower save that particular grid in winning grid
            if current_score <= protein.winning_score:
                protein.winning_grid = adapt_grid =  copy.deepcopy(protein.grid)
                protein.winning_coordinates = adapt_coordinates = copy.deepcopy(protein.coordinates)

                # update winning_score
                protein.winning_score = current_score

            # if the score is higher, calculate acceptance chance
            else:
                # calculate acceptance chance
                difference = protein.winning_score - current_score
                acceptance_chance = math.exp(difference / Ti)

                # generate random compare value
                value = randint(1,10000)/10000

                # if acceptance_chance <= value, the deterioration is not accepted
                if acceptance_chance < value:

                    # if not accepted, restore the old grid
                    protein.grid = copy.deepcopy(adapt_grid)
                    protein.coordinates = copy.deepcopy(adapt_coordinates)
                    current_score = old_score

                # if accepted
                else:
                    # update changes anyway in the grid
                    adapt_grid = copy.deepcopy(protein.grid)
                    adapt_coordinates = copy.deepcopy(protein.coordinates)

            # cool system linear
            Ti = T0 - 2 * ((i - minus) * (T0 - Tn) / N) + 0.001

    return [run_info, protein]
