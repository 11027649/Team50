
from utility.score import score
from utility.fold import fold

from algorithms.progress_bar import printProgressBar

from random import randint
import copy
import csv
import datetime

def hillclimber(protein):
    # will keep track of the score
    best_score = 0

    length = protein.protein_length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    iterations = 8000

    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        for j in range(14):
            random_value = get_random_value(1, protein.protein_length - 2)
            returncode_and_protein = fold(random_value[0], random_value[1], protein)
            protein = returncode_and_protein[1]

        stability = score(protein)

        # if the score is lower save that particular grid in winning grid
        if stability < best_score:
            protein.winning_grid = copy.deepcopy(protein.grid)
            protein.winning_coordinates = copy.deepcopy(protein.coordinates)
            best_score = stability
            protein.winning_score = best_score

        # else, restore the winning grid
        else:
            protein.grid = copy.deepcopy(protein.winning_grid)
            protein.coordinates = copy.deepcopy(protein.winning_coordinates)

    return protein


def fold_control_hillclimber(protein):
    """ Hillclimber which selects the best out of 14. """

    # will keep track of the score
    best_score = 0

    length = protein.protein_length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    iterations = 8000

    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        for j in range(14):
            random_value = get_random_value(1, protein.protein_length - 2)

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

    return protein

def extend_fold_hillclimber(protein):

    # will keep track of the score
    best_score = 0

    length = protein.protein_length
    protein.winning_grid = copy.deepcopy(protein.grid)
    protein.winning_coordinates = copy.deepcopy(protein.coordinates)

    iterations = 30

    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        extend = 2
        counter = 0
        found = False

        while found == False:

            for j in range(extend):

                random_value = get_random_value(1, protein.protein_length - 2)

                # do a valid fold
                returncode_and_protein = fold(random_value[0], random_value[1], protein)

                while returncode_and_protein[0] == "collision":

                    random_value = get_random_value(1, protein.protein_length - 2)

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
