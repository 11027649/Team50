from global_vars import amino
from score import score
from fold import fold
from print_protein import print_protein
import time
from random import randint


import global_vars
global_vars.init()

def hillclimber():

    # will keep track of the score
    best_score = global_vars.winning_score

    length = len(global_vars.protein_string)

    
    for i in range(10000):
        random_value = getrandvalue()
        fold(random_value[0], random_value[1])
        if score() < best_score:
            best_score = score()
            print_protein()
            print(score())

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
