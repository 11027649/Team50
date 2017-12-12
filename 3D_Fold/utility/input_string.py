# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: input_string.
#
# A function that allows the user to choose a protein.
# Takes: nothing, instead asks for input
# Updates: protein_string
# Calls: init_grid()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from utility.init_grid import init_grid

import global_vars
global_vars.init()

allowed_aminos = {"P", "H", "C"}
assignment_letter = []

def input_string():
    """ Ask the user for an input string and check if it meets the conditions for
        the input string. Calls the function init_grid to initialize the grid. """

    protein_input = input("Insert amino string or type assignment letter + number e.g. B2: ")

    # input must be 2 AA's or one of the assignements which are also 2 chars
    # (see assignements.txt)
    if len(protein_input) < 2:
        print("\nPlease enter at least 2 characters.\n")
        exit(1)
    else:
        # if the input starts with /, put it in protein_string no matter what
        if protein_input.startswith("/"):
            protein_string = protein_input[1:]

        # allow only the assignements strings, e.g. A1, B1-B4 and C1-C4
        elif not protein_input[0].isalpha() or (len(protein_input) > 2 and not protein_input[2:].isalpha()):
            print("\nOnly the second entry in the string can be a number. e.g. B2.\n")
            exit(1)

        # if the second char is not a digit, check for invalid AA's
        elif not protein_input[1].isdigit():
            for character in protein_input:
                char_upper = character.upper()
                if not char_upper in allowed_aminos:
                    print("\nThis string contains invalid amino characters.\n")
                    exit(1)
            protein_string = protein_input

        # if 2nd char is a digit, check which assignement
        elif (protein_input[1].isdigit()):
            if len(protein_input) > 2:
                print("\nThis string is not valid.\n")
                exit(1)

            protein_lines = open("inputFiles/assignments.txt").read().splitlines()
            
            # save protein input here in the file
            global_vars.csvfile.protein_name = protein_input

            # search for assignement
            for line in protein_lines:
                if line[0].upper() == protein_input[0].upper():
                    assignment_letter.append(line[4:])
                    protein_string = assignment_letter[0]
                if len(protein_input) == 2 and int(protein_input[1]) <= len(assignment_letter):
                    protein_string = assignment_letter[int(protein_input[1]) - 1]

            # quit if it doesn't exist
            if len(assignment_letter) < int(protein_input[1]):
                print("\nThis assignment does not exist.\n")
                exit(1)

        # print the users input and store in global vars (in uppercase letters)
        global_vars.protein.protein_string = protein_string.upper()

    init_grid()
