from message import message
from input_string import input_string
from print_protein import print_protein
from update_grid import update_grid
from fold import fold
from score import score
from hillclimber import hillclimber
from plotdata import plotdata
import copy

# import all the global variables
import global_vars
global_vars.init()

def main():
	""" This is a main function written for the hillclimber algorithm. It allows
		you to input how many times you want to run a hillclimber. For now it 
		returns from each hillclimber the best folded protein. """

	message("This is a protein-fold-optimizer by Team50")

	# get the user's choice of protein
	input_string()

	message("Protein received")

	hillclimber_times = int(input("How many times do you want to run this hillclimber algorithm? "))
	
	# print starting configuration of the protein
	print_protein()

	message("Protein initiated, starting algorithm.")

	winning_protein = [[hillclimber_times]]

	for i in range(hillclimber_times):
		hillclimber()
		# winning_protein[i] = copy.deepcopy(global_vars.coordinates)

		print("The best solution of the " + str(i) + "th hillclimber is the following protein, with a stability of: " + str(global_vars.winning_score))
		# print the best solution
		print_protein()


if __name__ == '__main__':
	main()