from visualization.message import message
from utility.input_string import input_string

from utility.update_grid import update_grid
from utility.fold import fold
from utility.score import score
from algorithms.hillclimber import hillclimber, fold_control_hillclimber, extend_fold_hillclimber
from algorithms.simulated_annealing import simulated_annealing, simulated_annealing_control
from algorithms.algo_brute_force import brute_force
from plotting.plots import plot_hillclimber, plot_best_protein, plot_simulated_annealing

import csv
from pygame import mixer

mixer.init()

# Import all the global variables.
import global_vars
global_vars.init()


def main():

    message("This is a protein-fold-optimizer by Team50")

    # Get the user's choice of protein.
    input_string()

    message("Protein received")

    algo_functions = {"Brute Force": brute_force, "Hill Climber": hillclimber, "Fold Control Hillclimber": fold_control_hillclimber, "Extend Fold Hillclimber": extend_fold_hillclimber, "Simulated Annealing": simulated_annealing, "Simulated Annealing Control": simulated_annealing_control}

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

    message("Protein initiated, algorithm chosen, please be patient.")

    mixer.music.load("elevator.mp3")
    mixer.music.play()

    algo_functions[algorithms[algorithm_choice]]()

    mixer.music.stop()

    print("Score: " + str(global_vars.protein.winning_score), end = '\n\n')
    plot_best_protein()

    if algorithms[algorithm_choice] == "Hill Climber":
        plot_hillclimber()

    if algorithms[algorithm_choice] == "Simulated Annealing":
        plot_simulated_annealing()



if __name__ == '__main__':
	main()
