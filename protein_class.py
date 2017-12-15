class Protein():
    def __init__(   self, protein_string, protein_length,
                    grid, coordinates, 
                    winning_grid, winning_coordinates,
                    winning_score, aminos):

        self.protein_string = protein_string
        self.length = protein_length

        self.grid = grid
        self.coordinates = coordinates
        
        self.winning_grid = winning_grid
        self.winning_coordinates = winning_coordinates
        
        self.winning_score = winning_score
        self.aminos = aminos

    def init_aminos(self):
        """ Puts the Aminos with an ID in a list. """

        for i in range(self.length):
            self.aminos.append(Amino(i, self.protein_string[i]))


    def init_grid(self):
        """ Initializes the grid with an x of protein length, y,z of 2. 
            Lays the protein horizontally in this grid. """

        # initialize the grid
        self.grid = [[[0 for i in range(2)] for j in range(2)] for k in range(self.length + 1)]
        
        # put aminos in grid
        for i in range(self.length - 1):
            self.grid[i][0][0] = self.aminos[i]

        # update coordinates
        self.coordinates = [[i ,0, 0] for i in range(self.length)]


class Amino():
    def __init__(self, num_id, letter):
        self.num_id = num_id
        self.letter = letter