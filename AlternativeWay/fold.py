# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: fold. A function that folds a protein. Does this by finding an
# origin and rotating the rest of the protein with a rotation matrix (left or 
# right), depending on the direction in which the protein is being fold.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import numpy as np
from update_grid import update_grid
from global_vars import amino

import global_vars
global_vars.init()

def fold(num_id, direction):
    """ Finds an origin to fold around and multiplies the coordinates of the aminos
        that will get a different place with a rotation matrix to get the new 
        coordinates. If the fold is not possible, returns and old grid and at which
        amino acid this fold was colliding. """

    coordinates = global_vars.coordinates
    backup_coordinates = coordinates[:]
    grid = global_vars.grid

    grid_height = len(grid[0])
    grid_width = len(grid)

<<<<<<< HEAD

    # print(num_id)
    # print(len(global_vars.protein_string), end="\n\n")
    length = len(global_vars.protein_string)
    if num_id >= length or num_id < 1:
        print("You try to fold on " + str(num_id) + ", only up to id " + str(length - 1) + " available.")
        # Returncode 1: trying to fold on a place that aint valid.
=======
    if num_id >= len(global_vars.protein_string) or num_id < 1:
        print("This fold index doesn't exist.")
        
        # returncode 1: an invalid place to fold
>>>>>>> c151632ddca14cc3ec9fe96b3c53374ca36db0d1
        return 1

    # find the rotation origin and print it's coordinates
    rot_origin = [coordinates[num_id][0], coordinates[num_id][1]]
<<<<<<< HEAD

    # print("Pivot origin: " + str(rot_origin[0]) + "," + str(rot_origin[1]))
=======
    print("Pivot origin: " + str(rot_origin[0]) + "," + str(rot_origin[1]))
>>>>>>> c151632ddca14cc3ec9fe96b3c53374ca36db0d1

    # set up rotation matrices
    rotation_matrix_left = [[0, 1], [-1, 0]]
    rotation_matrix_right = [[0, -1], [1, 0]]

<<<<<<< HEAD
    returncode = False

=======
    # for folds to Left or Right, set up the right rotation matrix
>>>>>>> c151632ddca14cc3ec9fe96b3c53374ca36db0d1
    if(direction == "R"):
        rotation_matrix = rotation_matrix_right
    elif(direction == "L"):
        rotation_matrix = rotation_matrix_left

    # iterates over the aminos, beginning at the one after the amino acid where
    # we'll fold
    for i in range(num_id + 1, len(global_vars.protein_string)):
        
        # cleans all aminos from where we'll fold
        grid[coordinates[i][0]][coordinates[i][1]] = 0

    # iterates over the aminos, beginning at the one after where we'll fold
    for i in range(num_id + 1, len(global_vars.protein_string)):

        from_coords = coordinates[i]
        to_coords = np.dot(rotation_matrix, np.subtract(from_coords, rot_origin))
                + rot_origin

        # expand grid if the fold made the protein to big to fit, and detect
        # foldings that aren't possible
        if (to_coords[0] < 0 or to_coords[0] >= grid_width):
            coordinates[i] = [to_coords[0], to_coords[1]]
        
        elif (to_coords[1] < 0 or to_coords[1] >= grid_height):
            coordinates[i] = [to_coords[0], to_coords[1]]
<<<<<<< HEAD
        elif (str(type(grid[to_coords[0]][to_coords[1]])) == "<class 'global_vars.amino'>"):
            # print("Collision detected while folding amino " + str(num_id) + "\n -> Stopped this fold, cause amino " + str(i) + " was colliding")
            coordinates = backup_coordinates
            returncode = True
            break
=======
        
        elif (str(type(grid[to_coords[0]][to_coords[1]])) == 
                    "<class 'global_vars.amino'>"):
            
            # print where the collision was detected
            print("Collision detected while folding amino " + str(num_id) 
                        + "\n -> Stopped this fold, cause amino " + str(i) + " was colliding")

            # reset coordinates and break out of the function
            coordinates = backup_coordinates
            break;
        
>>>>>>> c151632ddca14cc3ec9fe96b3c53374ca36db0d1
        else:
            coordinates[i] = [to_coords[0], to_coords[1]]

    # update global coordinates and update the grid
    global_vars.coordinates = coordinates
    update_grid()
<<<<<<< HEAD

    # print("rc: ", str(returncode))

    if returncode == True:
        return 1

    # if all_pos_free:
    #     # onthoud niewe grid en nieuwe coords in coordinates
    # if not all_pos_free:
    #     # onthoud oude grid en geef error shit mee
    #     # Returncode 2: fold collision
    #     print("Yeah you cannot fold this in this way cause that would collide")
    #     return 2
=======
>>>>>>> c151632ddca14cc3ec9fe96b3c53374ca36db0d1
