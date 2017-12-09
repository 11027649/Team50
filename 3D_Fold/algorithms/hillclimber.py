from global_vars import Amino
from utility.score import score
from utility.fold import fold

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
    # print("Hillclimbing...")

    global_vars.winning_score = 0

    # will keep track of the score
    best_score = global_vars.winning_score

    length = len(global_vars.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)

    iterations = 5000

    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filepath = "data\hillclimber\hc_" + str(date) + ".csv"
    global_vars.filepath = filepath

    # store data in .csv
    with open(filepath, 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)

        # do "iterations" random folds and keep track of the highest value
        for i in range(iterations):

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

#  hillclimber which selects the best out of 14
def fold_control_hillclimber():

    # will keep track of the score
    best_score = global_vars.winning_score = 0

    length = len(global_vars.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)

    iterations = 5000



    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        for j in range(14):
            random_value = get_random_value()

            while fold(random_value[0], random_value[1]) == "collision":
                random_value = get_random_value()



            stability = score()

            # if the score is lower save that particular grid in winning grid
            if stability < best_score:
                global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)
                best_score = stability
                global_vars.winning_score = best_score

                print("Best stability so far: " + str(best_score))
                print("iteration = " + str(j))
                print_protein()
                break
            # set the winning grid back as current grid
        global_vars.grid = copy.deepcopy(global_vars.winning_grid)
        global_vars.coordinates = copy.deepcopy(global_vars.winning_coordinates)


def extend_fold_hillclimber():

    global_vars.winning_score = 0

    # will keep track of the score
    best_score = global_vars.winning_score

    length = len(global_vars.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)

    iterations = 30

    # do "iterations" random folds and keep track of the highest value
    for i in range(iterations):

        print("Iteration: " + str(i))
        extend = 2
        counter = 0
        found = False

        while found == False:

            # print("Found: " + str(found))

            for j in range(extend):

                # print(" i ")

                random_value = get_random_value()

                # do a valid fold
                while fold(random_value[0], random_value[1]) == "collision":
                    random_value = get_random_value()

                # if the score is lower save that particular grid in winning grid

                stability = score()

                if stability < best_score:
                    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)
                    best_score = stability
                    global_vars.winning_score = best_score

                    print("Best stability so far: " + str(best_score))
                    print("Iteration: " + str(i))
                    print("Fold nr: " + str(j))
                    print("Extend amount: " + str(extend))
                    found = True
                    print_protein()
                    break

                counter += 1

                if counter > 1000:
                    extend += 1
                    counter = 0
                    # print("Extend amount: " + str(extend))

                print("                      extend: " + str(extend))
                if extend > 100:
                    exit(1)



        # set the winning grid back as current grid
        global_vars.grid = copy.deepcopy(global_vars.winning_grid)
        global_vars.coordinates = copy.deepcopy(global_vars.winning_coordinates)



def get_random_value():
    """ This is a function that returns an array with a random direction and 
        aminonumber, to make random folds. Also used in Simulated Annealing. """

    length = len(global_vars.protein_string) - 1
    aminonumber = randint(1, length)
    value = randint(0,1)
    direction = ""
    if value == 1:
        direction = "L"
    else:
        direction = "R"
    return [aminonumber, direction]
