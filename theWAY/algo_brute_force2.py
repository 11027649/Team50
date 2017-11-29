from global_vars import amino
from score import score
from fold import fold
from print_protein import print_protein
from print_protein import fancy_print_protein
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
