from random import randint
import copy
import csv
import math

def hillclimber2D(protein):
    # will keep track of the score
    best_score = 0

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    iterations = 8000
    # determines how much folds it will do
    folds = 14

    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        for j in range(folds):
            random_value = get_random_value(0, protein.length - 2)
            returncode_and_protein = protein.fold(random_value[0], random_value[1])

            # force a fold that is possible, and control if this is a better fold
            while returncode_and_protein[0] == "collision":
                random_value = get_random_value(0, protein.length - 2)
                returncode_and_protein = protein.fold(random_value[0], random_value[1])

            stability = protein.score()

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

    return protein

def hillclimber3D(protein):
    # will keep track of the score
    best_score = 0

    length = protein.length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    iterations = 8000
    # determines how much folds it will do
    folds = 14

    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        for j in range(folds):
            random_value = get_random_value(1, protein.length - 2)
            returncode_and_protein = protein.fold(random_value[0], random_value[1])

            # force a fold that is possible, and control if this is a better fold
            while returncode_and_protein[0] == "collision":
                random_value = get_random_value(1, protein.length - 2)
                returncode_and_protein = protein.fold(random_value[0], random_value[1])

            stability = protein.score()

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

    return protein

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