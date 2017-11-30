from global_vars import amino
from utility.score import score
from utility.fold import fold
from visualization.print_protein import print_protein

import time
import copy

import global_vars
global_vars.init()


def brute_force2():
    print("Brute forcing...")

    recursive(2)
    fold(1, "L")
    recursive(2)
    length = len(global_vars.protein_string)


def recursive(position):
