# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is part of the protein folding program made by Team50.
#
# It contains the main program. This is where the user is asked for input,
# their choices are saved, and the best protein and data are plotted.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from visualization.message import message

from utility.input_string import input_string

# import algorithms
from algorithms.hillclimber import hillclimber, fold_control_hillclimber, extend_fold_hillclimber
from algorithms.simulated_annealing import simulated_annealing, simulated_annealing_control, simulated_annealing_reheat
from algorithms.algo_brute_force import brute_force

# import plot tools
from plotting.plots import plot_data, plot_best_protein

from pygame import mixer
mixer.init()

def main():

    message("This is a protein-fold-optimizer by Team50")

    # get the user's choice of protein
    info_and_protein = input_string()
    run_info = info_and_protein[0]
    protein = info_and_protein[1]

    message("Protein received")

    # ask the user in which dimension they want to fold
    dimension = 2
    while not (dimension == 0) and not (dimension == 1):
        print("In what dimension do you want to fold? \n\n ( 0 ) 2D \n ( 1 ) 3D\n")
        dimension = int(input("Chosen dimension: "))

    # initialize the grid and save the dimension
    run_info.dimension = dimension
    protein.init_grid()

    # make a list with all the algorithms
    algo_functions = {"Brute Force": brute_force, "Hill Climber": hillclimber, \
        "Fold Control Hillclimber": fold_control_hillclimber, \
        "Extend Fold Hillclimber": extend_fold_hillclimber, \
        "Simulated Annealing": simulated_annealing, \
        "Simulated Annealing Control": simulated_annealing_control, \
        "Simulated Annealing Reheat": simulated_annealing_reheat}

    algorithms = []
    for key, value in algo_functions.items():
        algorithms.append(key)

    # ask the user which algorithm they want to run
    print("\nPlease choose which algorithm you want to apply.\n")

    for alg in algorithms:
        print(" ( " + str(algorithms.index(alg)) + " )   " + str(alg))
    print()

    algorithm_choice = len(algorithms)

    while algorithm_choice > len(algorithms) - 1:
        algorithm_choice = int(input("Chosen algorithm's number: "))

    message("Protein initiated, algorithm chosen, please be patient.")

    # play some music while waiting
    mixer.music.load("doc\elevator.mp3")
    mixer.music.play()

    # run the right algorithm
    info_and_protein = algo_functions[algorithms[algorithm_choice]](run_info, protein)
    run_info = info_and_protein[0]
    protein = info_and_protein[1]

    mixer.music.stop()
    mixer.music.load("doc\ping.mp3")
    mixer.music.play()

    message("Best score: " + str(protein.winning_score))

    # show the user the best found protein
    plot_best_protein(protein, run_info)

    # for all algorithms except brute force, plot the graphs
    if not algorithms[algorithm_choice] == "Brute Force":
        plot_data(run_info)

    message("End of program, thank you for using our application. \n     Find your generated data in the data folder. \n")


if __name__ == '__main__':
	main()
