# holds all the globals and stuff we need in every file

def init():
    global protein_string
    protein_string = ""
    global grid
    grid = []
    global coordinates
    coordinates = []
    global winning_coordinates
    winning_coordinates = []
    global winning_score
    winning_score = 0
    global winning_grid
    winning_grid = []
    global amount
    amount = 0

    global filepath
    filepath = ""

class amino():
    def __init__(self, num_id, letter):
        self.num_id = num_id
        self.letter = letter
