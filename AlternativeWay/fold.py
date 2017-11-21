# fold protein(id, direction)
import numpy as np
from update_grid import update_grid
from global_vars import amino

import global_vars
global_vars.init()

def fold(num_id, direction):

    coordinates = global_vars.coordinates
    backup_coordinates = coordinates[:]
    grid = global_vars.grid

    grid_height = len(grid[0]);
    grid_width = len(grid)


    # print(num_id)
    # print(len(global_vars.protein_string), end="\n\n")
    length = len(global_vars.protein_string)
    if num_id >= length or num_id < 1:
        print("You try to fold on " + str(num_id) + ", only up to id " + str(length - 1) + " available.")
        # Returncode 1: trying to fold on a place that aint valid.
        return 1

    rot_origin = [coordinates[num_id][0], coordinates[num_id][1]]

    # print("Pivot origin: " + str(rot_origin[0]) + "," + str(rot_origin[1]))

    rotation_matrix_left = [[0, 1], [-1, 0]]
    rotation_matrix_right = [[0, -1], [1, 0]]

    returncode = False

    if(direction == "R"):
        rotation_matrix = rotation_matrix_right
    elif(direction == "L"):
        rotation_matrix = rotation_matrix_left

    for i in range(num_id + 1, len(global_vars.protein_string)):
        # haal alle amino's in het grid weg achter vanaf waar we gaan vouwen
        grid[coordinates[i][0]][coordinates[i][1]] = 0

    for i in range(num_id + 1, len(global_vars.protein_string)):

        from_coords = coordinates[i]
        to_coords = np.dot(rotation_matrix, np.subtract(from_coords, rot_origin)) + rot_origin
        # pos_free = check_pos(to_coords)

        # gekke shit
        if (to_coords[0] < 0 or to_coords[0] >= grid_width):
            coordinates[i] = [to_coords[0], to_coords[1]]
        elif (to_coords[1] < 0 or to_coords[1] >= grid_height):
            coordinates[i] = [to_coords[0], to_coords[1]]
        elif (str(type(grid[to_coords[0]][to_coords[1]])) == "<class 'global_vars.amino'>"):
            # print("Collision detected while folding amino " + str(num_id) + "\n -> Stopped this fold, cause amino " + str(i) + " was colliding")
            coordinates = backup_coordinates
            returncode = True
            break
        else:
            coordinates[i] = [to_coords[0], to_coords[1]]

    global_vars.coordinates = coordinates

    update_grid()

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
