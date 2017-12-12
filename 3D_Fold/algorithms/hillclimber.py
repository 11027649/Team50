from global_vars import Amino
from utility.score import score
from utility.fold import fold
from algorithms.progress_bar import printProgressBar

import time
import os
from random import randint
import copy
import csv
import datetime

import global_vars
global_vars.init()

def hillclimber():
    # if accept is True, folds that collide will count
    # if False only folds that pass will happen
    accept = False

    global_vars.protein.winning_score = 0

    # will keep track of the score
    best_score = global_vars.protein.winning_score

    length = len(global_vars.protein.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

    iterations = 5000

    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filepath = "data\hillclimber\hc_" + str(date) + ".csv"
    global_vars.filepath = filepath

    # store data in .csv
    with open(filepath, 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

            printProgressBar(i, iterations)

            datawriter.writerow([i] + [best_score])

            for j in range(6):
                random_value = get_random_value()
                if accept == True:
                    fold(random_value[0], random_value[1])
                else:
                    while fold(random_value[0], random_value[1]) == "collision":
                        random_value = get_random_value()

            stability = score()

            # if the score is lower save that particular grid in winning grid
            if stability < best_score:
                global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)
                best_score = stability
                global_vars.protein.winning_score = best_score

            else:
                global_vars.grid = copy.deepcopy(global_vars.winning_grid)
                global_vars.protein.coordinates = copy.deepcopy(global_vars.protein.winning_coordinates)

    os.system("cls")


def fold_control_hillclimber():
    """ Hillclimber which selects the best out of 14. """

    # will keep track of the score
    best_score = global_vars.protein.winning_score = 0

    length = len(global_vars.protein.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

    iterations = 5000

    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        printProgressBar(i, iterations)

        for j in range(14):
            random_value = get_random_value()

            while fold(random_value[0], random_value[1]) == "collision":
                random_value = get_random_value()

            stability = score()

            # if the score is lower save that particular grid in winning grid
            if stability < best_score:
                global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)
                best_score = stability
                global_vars.protein.winning_score = best_score

                break
            # set the winning grid back as current grid
        global_vars.grid = copy.deepcopy(global_vars.winning_grid)
        global_vars.protein.coordinates = copy.deepcopy(global_vars.protein.winning_coordinates)


def extend_fold_hillclimber():

    global_vars.winning_score = 0

    # will keep track of the score
    best_score = global_vars.protein.winning_score

    length = len(global_vars.protein.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

    iterations = 30

    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        extend = 2
        counter = 0
        found = False

        while found == False:

            for j in range(extend):

                printProgressBar(extend, 101)

                random_value = get_random_value()

                # do a valid fold
                while fold(random_value[0], random_value[1]) == "collision":
                    random_value = get_random_value()

                # if the score is lower save that particular grid in winning grid

                stability = score()

                if stability < best_score:
                    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)
                    best_score = stability
                    global_vars.protein.winning_score = best_score

                    found = True

                    break

                counter += 1

                if counter > 1000:
                    extend += 1
                    counter = 0

                if extend > 100:
                    return

        # set the winning grid back as current grid
        global_vars.grid = copy.deepcopy(global_vars.winning_grid)
        global_vars.protein.coordinates = copy.deepcopy(global_vars.protein.winning_coordinates)


def get_random_value():
    """ This is a function that returns an array with a random direction and
        aminonumber, to make random folds. Also used in Simulated Annealing. """

    length = len(global_vars.protein.protein_string) - 2
    aminonumber = randint(1, length)
    value = randint(0,3)
    direction = ""
    if value == 1:
        direction = "L"
    elif value == 2:
        direction = "R"
    elif value == 3:
        direction = "U"
    else:
        direction = "D"
    return [aminonumber, direction]
