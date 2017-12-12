# holds all the globals and stuff we need in every file

def init():
    global grid
    grid = []
    global winning_grid
    winning_grid = []
    global amount
    amount = 0

    global filepath
    filepath = ""

    global protein
    protein = Protein("", [], [], 0, [])

# class File():
#     def __init__(self, filepath):
#         self.filepath = filepath

#     def generate_filename():


class Protein():
    def __init__(self, protein_string, coordinates, winning_coordinates,
        winning_score, aminos):
        self.protein_string = protein_string
        self.coordinates = coordinates
        self.winning_coordinates = winning_coordinates
        self.winning_score = winning_score
        self.aminos = aminos

    # def initialize():


class Amino():
    def __init__(self, num_id, letter):
        self.num_id = num_id
        self.letter = letter
