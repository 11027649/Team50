def print_coordinates(protein):
    """ Prints the coordinates of all aminos of the protein.
        Used for debugging purposes. """

    # loop over all amino acids and print coordinates
    for i in range(len(protein)):
        print ("x = " + str(protein[i].aa_x), end ='')
        print (" y = " + str(protein[i].aa_y), end ='')
        print (" direction = " + str(protein[i].direction), end ='')
        print()

def print_protein(grid):
    """ Prints the protein in the grid, without extra styling (like -- for 
        bonds) """
    
    # set up variables
    max_x = len(grid)
    max_y = len(grid[1])

    # loop over x and y
    for i in range(max_y):
        for j in range(max_x):

            # if not empty grid spot, print letter, else print grid spot
            if not grid[j][i] == ' ':
                print (grid[j][i].letter, end ='')
            else:
                print (grid[j][i], end ='')

        # print enter for next row
        print()