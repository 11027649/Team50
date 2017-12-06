from global_vars import amino
from utility.score import score
from utility.fold import fold
from visualization.print_protein import print_protein

import time
import os
from random import randint
import copy
import csv
import math

import global_vars
global_vars.init()

def simulated_annealing():

    global_vars.winning_score = current_score = 0

    length = len(global_vars.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)

    # initialize iterations, begin and end temperature
    N = 5000
    T0 = Ti = 1
    Tn = 0

    # store data in .csv
    with open('simulated_annealing.csv', 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)

        # do N times 3 random folds and keep track of the best value
        for i in range(N):

            # write score and iteration to a csv file
            datawriter.writerow([i] + [current_score])

            # do random folds
            for j in range(10):
                random_value = get_random_value()
                return_code = fold(random_value[0], random_value[1])

            # calculate stability of the protein
            current_score = score()

            # if the score is lower save that particular grid in winning grid
            if current_score <= global_vars.winning_score:
                global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)
            
                global_vars.winning_score = current_score

                print("Best stability so far: " + str(global_vars.winning_score))


            # if the score is higher, calculate acceptance chance
            else:
                # calculate acceptance chance
                difference = global_vars.winning_score - current_score

                acceptance_chance = math.exp(difference / Ti)

                print("Acceptance chance = " + str(acceptance_chance) + "\n")

                value = randint(1,10000)/10000
                print("Compare value (randint) = ", value)
                
                # FIX DIT DAT HET MOOI WORDT
                # not accepted
                if acceptance_chance <= value:
                    # if not accepted, store the changes anyway in winning_grid
                    hoi = 1

                else:
                    global_vars.grid = copy.deepcopy(global_vars.winning_grid)
                    global_vars.coordinates = copy.deepcopy(global_vars.winning_coordinates)

                    print("                                                         Accepted")

            print("winning_score: ", global_vars.winning_score, "current score: ", current_score)
            # print_protein()

            # cool system
            Ti = T0 - (i * (T0 - Tn) / N)
            print("Current temperature = " + str(Ti))


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
