# holds all the globals and stuff we need in every file

def init():
    global protein_string
    protein_string = ""
    global grid
    grid = []
    global coordinates
    coordinates = []

class amino():
    def __init__(self, num_id, letter, x, y):
        self.num_id = num_id
        self.letter = letter
        self.x = x
        self.y = y
