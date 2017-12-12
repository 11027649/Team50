# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Contains: print_mess. A function that prints out a special, easy to recognize,
# message to theirselves.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def message(to_print):
	""" Prints a message to show the user where in the program he/she is. """

	main_indicator = "\n>>>> "
	print(main_indicator + to_print, end="\n\n")
