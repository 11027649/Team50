from utility.update_grid import update_grid

import numpy as np
import copy

class Protein():

    def __init__(   self, protein_string, protein_length,
                    grid, coordinates,
                    winning_grid, winning_coordinates,
                    winning_score, aminos):

        self.protein_string = protein_string
        self.length = protein_length

        self.grid = grid
        self.coordinates = coordinates

        self.winning_coordinates = winning_coordinates
        self.winning_grid = winning_grid

        self.winning_score = winning_score
        self.aminos = aminos

    def init_aminos(self):
        """ Puts the Aminos with an ID in a list. """

        for i in range(self.length):
            self.aminos.append(Amino(i, self.protein_string[i]))


    def init_grid(self):
        """ Initializes the grid with an x of protein length, y,z of 2.
            Lays the protein horizontally in this grid. """

        self.init_aminos()

        # initialize the grid
        self.grid = [[[0 for i in range(2)] for j in range(2)] for k in range(self.length + 1)]

        # put aminos in grid
        for i in range(self.length - 1):
            self.grid[i][0][0] = self.aminos[i]

        # update coordinates
        self.coordinates = [[i ,0, 0] for i in range(self.length)]


    def score(self):
        """ A function that returns a stability score for a specific folding of a
        protein. Does this by taking the global grid, coordinates and protein
        string. """

        score = 0
        grid = self.grid
        coordinates = self.coordinates

        # for all aminos in the protein
        for i in range(self.length):

            # the coordinates are stored in an array. i is the amino acid that you're
            # looking for, [0] or [1] are x and y
            x = coordinates[i][0]
            y = coordinates[i][1]
            z = coordinates[i][2]


            # initialize the first coordinate independent of direction
            coor1 = grid[x][y][z]

            # if it's an H, do something with the score
            # check only under and to the right to not count interactions double
            if not coor1.letter == "P":
                if type(coor1) == Amino:

                    # initialize the second coordinate depending on the direction
                    coor2x = grid[x + 1][y][z]
                    coor2y = grid[x][y + 1][z]
                    coor2z = grid[x][y][z + 1]

                    # will check if there is a score between coor1 and coor2
                    score -= self.calc_score(coor1, coor2x)
                    score -= self.calc_score(coor1, coor2y)
                    score -= self.calc_score(coor1, coor2z)

        return score


    def calc_score(self, coor1, coor2):
        if type(coor2) == Amino \
            and not coor2.letter == "P" \
            and abs(coor1.num_id - coor2.num_id) > 1:

            if coor2.letter == coor1.letter:
                if coor2.letter == "C":
                    return 5
                else:
                    return 1
            else:
                return 1
        return 0


    def fold(self, num_id, direction):
        """ Finds an origin to fold around and multiplies the coordinates of the aminos
            that will get a different place with a rotation matrix to get the new
            coordinates. If the fold is not possible, returns and old grid and at which
            amino acid this fold was colliding. """

        coordinates = self.coordinates
        backup_coordinates = coordinates[:]
        grid = self.grid

        protein_length = self.length
        grid_x = len(grid)
        grid_y = len(grid[0])
        grid_z = len(grid[0][0])
        # print("IN FOLD, x, y, z: ", grid_x, grid_x, grid_z)

        length = protein_length
        if num_id >= length or num_id < 1:
            print("You try to fold on " + str(num_id) + ", only up to id " + str(length - 1) + " available.")

        if num_id >= protein_length or num_id < 1:
            print("This fold index doesn't exist.")

            # returncode 2: an invalid place to fold
            return "out of range"

        # find the rotation origin and print it's coordinates
        rot_origin = [coordinates[num_id][0], coordinates[num_id][1], coordinates[num_id][2]]

        # print("Pivot origin: ", rot_origin[0], ",", rot_origin[1], ",", rot_origin[2])

        # rotations matrixes around z axis
        rotation_matrix_down_z = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        rotation_matrix_up_z = [[0, 1, 0], [-1, 0, 0],[0, 0, 1]]

        # rotations around y axis
        rotation_matrix_up_y = [[0, 0, -1], [0, 1, 0],[1, 0, 0]]
        rotation_matrix_down_y = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]

        # rotations around x axis
        rotation_matrix_down_x = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
        rotation_matrix_up_x = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]

        returncode = False

        # determine the axis of rotations
        next_coords = [coordinates[num_id + 1][0], coordinates[num_id + 1][1], coordinates[num_id + 1][2]]

        axis = ""

        if (next_coords[0] != rot_origin[0]):
            if (direction == "R"):
                rotation_matrix = rotation_matrix_up_z
            elif (direction == "L"):
                rotation_matrix = rotation_matrix_down_z
            elif (direction == "U"):
                rotation_matrix = rotation_matrix_up_y
            elif (direction == "D"):
                rotation_matrix = rotation_matrix_down_y

        elif (next_coords[1] != rot_origin[1]):
            if (direction == "R"):
                rotation_matrix = rotation_matrix_up_z
            elif (direction == "L"):
                rotation_matrix = rotation_matrix_down_z
            elif (direction == "U"):
                rotation_matrix = rotation_matrix_up_x
            elif (direction == "D"):
                rotation_matrix = rotation_matrix_down_x

        elif (next_coords[2] != rot_origin[2]):
            if (direction == "R"):
                rotation_matrix = rotation_matrix_up_y
            elif (direction == "L"):
                rotation_matrix = rotation_matrix_down_y
            elif (direction == "U"):
                rotation_matrix = rotation_matrix_up_x
            elif (direction == "D"):
                rotation_matrix = rotation_matrix_down_x

        # iterates over the aminos, beginning at the one after the amino acid where
        # we'll fold
        for i in range(num_id + 1, protein_length):

            # cleans all aminos from where we'll fold
            grid[coordinates[i][0]][coordinates[i][1]][coordinates[i][2]] = 0

        # iterates over the aminos, beginning at the one after where we'll fold
        for i in range(num_id + 1, protein_length):

            from_coords = coordinates[i]

            subtracted = np.subtract(from_coords, rot_origin)
            to_coords = np.dot(rotation_matrix, subtracted) + rot_origin

            # expand grid if the fold made the protein to big to fit, and detect
            # foldings that aren't possible
            if (to_coords[0] < 0 or to_coords[0] >= grid_x):
                coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

            elif (to_coords[1] < 0 or to_coords[1] >= grid_y):
                coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

            elif (to_coords[2] < 0 or to_coords[2] >= grid_z):
                coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

            # if fold isn't possible
            elif (type(grid[to_coords[0]][to_coords[1]][to_coords[2]]) == Amino):
                
                coordinates = backup_coordinates[:]
                returncode = True
                break

            else:
                coordinates[i] = [to_coords[0], to_coords[1], to_coords[2]]

        # update global coordinates and update the grid
        self.coordinates = coordinates[:]
        update_grid(self)

        if returncode == True:
            return ["collision", self]
        else:
            return [0, self]


class Amino():
    def __init__(self, num_id, letter):
        self.num_id = num_id
        self.letter = letter
