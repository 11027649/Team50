from global_vars import amino
from utility.score import score
from utility.fold import fold
from visualization.print_protein import print_protein

import time
import os
from random import randint
import copy
import csv

import global_vars
global_vars.init()

def hillclimber():

    # print("Hillclimbing...")

    global_vars.winning_score = 0

    # will keep track of the score
    best_score = global_vars.winning_score

    length = len(global_vars.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)

    iterations = 5000

    # store data in .csv
    with open('result files/hillclimber.csv', 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

            datawriter.writerow([i] + [best_score])

            for j in range(3):
                random_value = get_random_value()
                return_code = fold(random_value[0], random_value[1])


            stability = score()

                # if the score is lower save that particular grid in winning grid
            if stability < best_score:
                global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)
                best_score = stability
                global_vars.winning_score = best_score

                os.system("cls")
                print("Best stability so far: " + str(best_score))
                print_protein()
                time.sleep(0.5)

            else:
                global_vars.grid = copy.deepcopy(global_vars.winning_grid)
                global_vars.coordinates = copy.deepcopy(global_vars.winning_coordinates)

    os.system("cls")


# return an array with a random direction and aminonumber
def get_random_value():
    length = len(global_vars.protein_string) - 1
    aminonumber = randint(1, length)
    value = randint(0,1)
    direction = ""
    if value == 1:
        direction = "L"
    else:
        direction = "R"
    return [aminonumber, direction]
