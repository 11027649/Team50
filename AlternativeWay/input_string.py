# this file contains a function for the user's choise of protein
from init_grid import init_grid

import global_vars
global_vars.init()

allowed_aminos = {"P", "H", "C"}

assignment_letter = []

def input_string():

    protein_input = input("Insert amino string or type assignment letter + number e.g. B2: ")

    if len(protein_input) < 2:
        print("\nPlease enter at least 2 characters.\n")
        exit(1)
    else:
        if protein_input.startswith("/"):
            protein_string = protein_input[1:]
        elif not protein_input[0].isalpha() or (len(protein_input) > 2 and not protein_input[2:].isalpha()):
            print("\nOnly the second entry in the string can be a number. e.g. B2.\n")
            exit(1)
        elif not protein_input[1].isdigit():
            for character in protein_input:
                char_upper = character.upper()
                if not char_upper in allowed_aminos:
                    print("\nThis string contains invalid amino characters.\n")
                    exit(1)
            protein_string = protein_input
        elif (protein_input[1].isdigit()):
            if len(protein_input) > 2:
                print("\nThis string is not valid.\n")
                exit(1)
            protein_lines = open("assignments.txt").read().splitlines()
            for line in protein_lines:
                if line[0].upper() == protein_input[0].upper():
                    assignment_letter.append(line[4:])
                    protein_string = assignment_letter[0]
                if len(protein_input) == 2 and int(protein_input[1]) <= len(assignment_letter):
                    protein_string = assignment_letter[int(protein_input[1]) - 1]

            if len(assignment_letter) < int(protein_input[1]):
                print("\nThis assignment does not exist.\n")
                exit(1)

        print("\nInputted: " + protein_string)

        global_vars.protein_string = protein_string.upper()

    init_grid()
    # protein_string = ord(protein_input[0].upper()) - 65 + int(protein_input[1])
    # print(protein_string)
