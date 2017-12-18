# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is part of the protein folding program made by Team50.
# 
# Contains a function that prints out a special, easy to recognize, message 
# to the user.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def message(to_print):
	""" Prints a special message to the user. """

	main_indicator = "\n>>>> "
	print(main_indicator + to_print, end="\n\n")
