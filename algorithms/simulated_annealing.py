from utility.score import score
from utility.fold import fold

from algorithms.hillclimber import get_random_value
from algorithms.progress_bar import printProgressBar

import datetime

from random import randint
import copy
import csv
import math


def simulated_annealing(run_info, protein):

    length = protein.protein_length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 10000
    T0 = Ti = 1
    Tn = 0
    current_score = 0

    # store algorithm in file, write a header
    run_info.algorithm = "Simulated Annealing"

    # generate a filepath
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    run_info.filepath = "data\hillclimber\sa_" + str(date) + ".csv"

    # store data in .csv
    with open(run_info.filepath, 'w', newline='') as datafile:
        datawriter = csv.writer(datafile)
        datawriter.writerow(["# This is a datafile generated for protein: " + str(protein.protein_string)])
        datawriter.writerow(["# It is generated with a" +  run_info.algorithm + "algorithm."])

        # do N times 10 random folds and keep track of the best value
        for i in range(N):

            printProgressBar(i, N)

            # write score and iteration to a csv file
            datawriter.writerow([i] + [current_score])

            # do random folds
            for j in range(10):
                random_value = get_random_value(run_info.dimension, protein.protein_length - 2)
                returncode_and_protein = fold(random_value[0], random_value[1], protein)
                protein = returncode_and_protein[1]

            old_score = current_score
            # calculate stability of the protein
            current_score = score(protein)

            # if the score is lower save that particular grid in winning grid
            if current_score <= protein.winning_score:
                protein.winning_grid = copy.deepcopy(protein.grid)
                protein.winning_coordinates = copy.deepcopy(protein.coordinates)

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
                    protein.grid = copy.deepcopy(protein.winning_grid)
                    protein.coordinates = copy.deepcopy(protein.winning_coordinates)
                    current_score = old_score

                # if accepted
                else:
                    # update changes anyway in the grid
                    protein.winning_grid = copy.deepcopy(protein.grid)
                    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

            # cool system linear
            Ti = T0 - (i * (T0 - Tn) / N)
    
    return [run_info, protein]


def simulated_annealing_control(run_info, protein):
    protein.winning_score = current_score = 0

    length = protein.protein_length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 10000
    T0 = Ti = 1
    Tn = 0

    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filepath = "data\simulated_annealing\sa_fc" + str(date) + ".csv"
    run_info.filepath = filepath
    run_info.algorithm = "Simulated Annealing (with fold control)"

    # store data in .csv
    with open(filepath, 'w', newline='') as datafile:
        datawriter = csv.writer(datafile)
        datawriter.writerow(["# This is a datafile generated for protein: " + str(protein.protein_string)])
        datawriter.writerow(["# It is generated with a Simulated Annealing with fold control algorithm."])

        # do N times 3 random folds and keep track of the best value
        for i in range(N):

            printProgressBar(i, N)

            # write score and iteration to a csv file
            datawriter.writerow([i] + [current_score])

            # do .. random folds and check each fold for a better score
            for j in range(10):
                # initial random value
                random_value = get_random_value(run_info.dimension, protein.protein_length - 2)

                returncode_and_protein = fold(random_value[0], random_value[1], protein)

                # while  returncode_and_protein[0] == "collision":
                #     random_value = get_random_value(run_info.dimension, protein.protein_length - 2)
                #     returncode_and_protein = fold(random_value[0], random_value[1], protein)

                protein = returncode_and_protein[1]

                old_score = current_score
                # calculate stability of the protein
                current_score = score(protein)

                # if the score is lower save that particular grid in winning grid
                if current_score < protein.winning_score:
                    protein.winning_grid = copy.deepcopy(protein.grid)
                    protein.winning_coordinates = copy.deepcopy(protein.coordinates)
                    protein.winning_score = current_score

                else:
                    # calculate acceptance chance
                    difference = protein.winning_score - current_score
                    acceptance_chance = math.exp(difference / Ti)

                    # generate random compare value
                    value = randint(1,10000)/10000

                    # if acceptance_chance <= value, the deterioration is not accepted
                    if acceptance_chance < value:

                        # if not accepted, restore the old grid
                        protein.grid = copy.deepcopy(protein.winning_grid)
                        protein.coordinates = copy.deepcopy(protein.winning_coordinates)
                        current_score = old_score

                    # if accepted
                    else:
                        # update changes anyway in the grid
                        protein.winning_grid = copy.deepcopy(protein.grid)
                        protein.winning_coordinates = copy.deepcopy(protein.coordinates)

        # cool system linear
        Ti = T0 - (i * (T0 - Tn) / N)

    return [run_info, protein]
