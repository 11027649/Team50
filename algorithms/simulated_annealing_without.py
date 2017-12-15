from utility.score import score
from utility.fold import fold

from algorithms.hillclimber import get_random_value
from algorithms.progress_bar import printProgressBar

import datetime

from random import randint
import copy
import csv
import math


def simulated_annealing(protein):

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 8000
    T0 = Ti = 1
    Tn = 0
    current_score = 0

    # do N times 10 random folds and keep track of the best value
    for i in range(N):

        # do random folds
        for j in range(14):
            random_value = get_random_value(1, protein.plength - 2)
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
    
    return protein


def simulated_annealing_control(protein):

    current_score = 0

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 8000
    T0 = Ti = 1
    Tn = 0

    # do N times 3 random folds and keep track of the best value
    for i in range(N):

        # do .. random folds and check each fold for a better score
        for j in range(14):
            # initial random value
            random_value = get_random_value(1, protein.length - 2)
            returncode_and_protein = fold(random_value[0], random_value[1], protein)
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

    return protein
