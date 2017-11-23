from global_vars import amino
from score import score
from fold import fold
from print_protein import print_protein
import time
from random import randint
import copy
import csv

import global_vars
global_vars.init()

def hillclimber():

    # will keep track of the score
    best_score = global_vars.winning_score

    length = len(global_vars.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)


    with open('data.csv', 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)

        # do 1000 random folds and keep track of the highest value
        for i in range(1000):

            # store data in .csv
            datawriter.writerow([i] + [best_score])
            
            for j in range(5):
                random_value = getrandvalue()
                fold(random_value[0], random_value[1])

            # if the score is lower save that particular grid in winning grid
            if score() < best_score:
                global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                global_vars.winning_coordinates = copy.deepcopy(global_vars.coordinates)
                best_score = score()
                print_protein()
                print(score())

            else:
                global_vars.grid = copy.deepcopy(global_vars.winning_grid)
                global_vars.coordinates = copy.deepcopy(global_vars.winning_coordinates)


# return an array with a random direction and aminonumber
def getrandvalue():
    length = len(global_vars.protein_string) - 1
    aminonumber = randint(1, length)
    value = randint(0,1)
    direction = ""
    if value == 1:
        direction = "L"
    else:
        direction = "R"
    return [aminonumber, direction]
