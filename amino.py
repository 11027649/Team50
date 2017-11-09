# save position of each amino acid to remember which ones are linked
class Amino():
    def __init__(self, letter, pos_next, aa_x, aa_y):
        self.letter = letter
        self.pos_next = pos_next
        self.aa_x = aa_x
        self.aa_y = aa_y