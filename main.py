from visualization.message import message
from utility.input_string import input_string
from visualization.print_protein import print_protein
from utility.update_grid import update_grid
from utility.fold import fold
from utility.score import score
from algorithms.hillclimber import hillclimber
from algorithms.simulated_annealing import simulated_annealing
from algorithms.algo_brute_force import brute_force
from plotting.plots import plothillclimber, plot_best_protein

import csv

# Import all the global variables.
import global_vars
global_vars.init()


def main():

    message("This is a protein-fold-optimizer by Team50")

    # Get the user's choice of protein.
    input_string()

    message("Protein received")

    # Print starting configuration of the protein
    print_protein()

    algo_functions = {"Brute Force": brute_force, "Hill Climber": hillclimber, "Simulated Annealing": simulated_annealing}

    algorithms = []
    for key, value in algo_functions.items():
        algorithms.append(key)

    print("Please choose which algorithm you want to apply.")

    for alg in algorithms:
        print(" ( " + str(algorithms.index(alg)) + " )   " + str(alg))
    print()

    algorithm_choice = len(algorithms)

    while algorithm_choice > len(algorithms) - 1:
        algorithm_choice = int(input("Chosen algorithm's number: "))

    message("Protein initiated, algorithm chosen, starting algorithm now.")

    algo_functions[algorithms[algorithm_choice]]()

    print_protein()
    print("Score: " + str(global_vars.winning_score), end = '\n\n')
    plot_best_protein()

    if algorithms[algorithm_choice] == "Hill Climber":
        plothillclimber()



if __name__ == '__main__':
	main()
