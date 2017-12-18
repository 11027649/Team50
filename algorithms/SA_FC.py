from algorithms.hillclimber import get_random_value

from random import randint
import copy
import csv
import math

def simulated_annealing_control2D(protein):

    length = protein.length
    protein.winning_grid = adapt_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = adapt_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 8000
    T0 = Ti = 1
    Tn = 0
    current_score = 0

    folds = 14

    adapt_score = 0

    # do N times 14 random folds and keep track of the best value
    for i in range(N):

        # this variable checks if a better score is found in 14 folds
        found_better = False
        old_score = current_score

        # do .. random folds and check each fold for a better score
        for j in range(folds):
            # initial random value
            random_value = get_random_value(0, protein.length - 2)
            returncode_and_protein = protein.fold(random_value[0], random_value[1])

            while returncode_and_protein[0] == "collision":
                random_value = get_random_value(0, protein.length - 2)
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

    return protein

def simulated_annealing_control3D(protein):

    length = protein.length
    protein.winning_grid = adapt_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = adapt_coordinates = copy.deepcopy(protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 8000
    T0 = Ti = 1
    Tn = 0
    current_score = 0

    folds = 14

    adapt_score = 0

    # do N times 14 random folds and keep track of the best value
    for i in range(N):

        # this variable checks if a better score is found in 14 folds
        found_better = False
        old_score = current_score

        # do .. random folds and check each fold for a better score
        for j in range(folds):
            # initial random value
            random_value = get_random_value(1, protein.length - 2)
            returncode_and_protein = protein.fold(random_value[0], random_value[1])

            while returncode_and_protein[0] == "collision":
                random_value = get_random_value(1, protein.length - 2)
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

    return protein