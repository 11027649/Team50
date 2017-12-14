from visualization.message import message

from utility.input_string import input_string
from utility.init_grid import init_grid

from protein_class import Protein

# import algorithms
from algorithms.hillclimber_zonder import hillclimber, fold_control_hillclimber, extend_fold_hillclimber
from algorithms.simulated_annealing_zonder import simulated_annealing, simulated_annealing_control

import csv

def main():

    # run 100 hillclimbers for protein C1
    with open('C1_3D_HC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Hillclimber: " + str(i))

            protein_string = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein = init_grid(protein)

            protein = hillclimber(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

    # run 100 hillclimbers with fold control for protein C1
    with open('C1_3D_HC_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Hillclimber with fold control: " + str(i))

            protein_string = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein = init_grid(protein)

            protein = fold_control_hillclimber(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

        # run 100 hillclimbers with fold control for protein C1
    with open('C1_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Hillclimber with fold control: " + str(i))

            protein_string = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein = init_grid(protein)

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

        # run 100 hillclimbers with fold control for protein C1
    with open('C1_3D_SA_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Hillclimber with fold control: " + str(i))

            protein_string = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein = init_grid(protein)

            protein = simulated_annealing_control(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

if __name__ == '__main__':
	main()
