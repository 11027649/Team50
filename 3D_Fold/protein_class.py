class Protein():
    def __init__(   self, protein_string, protein_length,
                    grid, coordinates, 
                    winning_grid, winning_coordinates,
                    winning_score, aminos):

        self.protein_string = protein_string
        self.protein_length = protein_length

        self.grid = grid
        self.coordinates = coordinates
        
        self.winning_grid = winning_grid
        self.winning_coordinates = winning_coordinates
        
        self.winning_score = winning_score
        self.aminos = aminos

    # def initialize(): string aminos omzetten in lijst


class Amino():
    def __init__(self, num_id, letter):
        self.num_id = num_id
        self.letter = letter