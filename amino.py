# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# contains the Class Amino
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Amino():
	""" Contains all information of the Amino Acids in a protein. """

	def __init__(self, letter, pos_next, aa_x, aa_y, direction):
		self.letter = letter
		self.pos_next = pos_next
		self.aa_x = aa_x
		self.aa_y = aa_y
		self.direction = direction
