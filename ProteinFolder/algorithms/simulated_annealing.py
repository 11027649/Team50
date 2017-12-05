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

def simulated_annealing():

    global_vars.winning_score = 0

    # will keep track of the score
    best_score = global_vars.winning_score

    length = len(global_vars.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)

    # initialize iterations, begin and end temperature
    N = 5000
    T0 = Ti = 1000
    Tn = 0

    # store data in .csv
    with open('simulated_annealing.csv', 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)

        # do N times 3 random folds and keep track of the best value
        for i in range(N):

            # write score and iteration to a csv file
            datawriter.writerow([i] + [best_score])

            # do random folds
            for j in range(3):
                random_value = get_random_value()
                return_code = fold(random_value[0], random_value[1])

            # calculate stability of the protein
            current_score = score()

            # if the score is lower save that particular grid in winning grid
            if current_score < best_score:
                global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)
            
                global_vars.winning_score = current_score

                print("Best stability so far: " + str(best_score))


            # if the score is higher, calculate acceptance chance
            else:
                # calculate acceptance chance
                difference = winning_score - current_score
                acceptance_chance = Math.exp(difference/Ti)
                print("Acceptance chance = " + acceptance_chance + "\n")

                if acceptance_chance > randint(0,100):
                    # if accepted, store the changes anyway in winning_grid
                    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)
                    best_score = stability
                    global_vars.winning_score = best_score

                else:
                    # if not accepted, restore the old grid
                    global_vars.grid = copy.deepcopy(global_vars.winning_grid)
                    global_vars.coordinates = copy.deepcopy(global_vars.winning_coordinates)

            print_protein()

            # cool system
            Ti = T0 - i(T0 - Tn) / N
            print("Current temperature = " + Ti)


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

def main():
    # Get the user's choice of protein.
    input_string()

    message("Protein received")

    # Print starting configuration of the protein
    print_protein()

    simulated_annealing()

if __name__ == '__main__':
    main()