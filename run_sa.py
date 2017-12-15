from visualization.message import message

from utility.input_string import input_string
from utility.init_grid import init_grid

from protein_class import Protein

# import algorithms
from algorithms.hillclimber_without import hillclimber, fold_control_hillclimber
from algorithms.simulated_annealing_without import simulated_annealing, simulated_annealing_control

import csv

def main():

    # run 50 simulated annealing for protein C1
    with open('C1_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Simulated Annealing: " + str(i))

            protein_string = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein = init_grid(protein)

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

    # run 50 simulated annealing for protein C1
    with open('C2_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Simulated Annealing: " + str(i))

            protein_string = "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein = init_grid(protein)

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

    # run 50 simulated annealing for protein C1
    with open('C3_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Simulated Annealing: " + str(i))

            protein_string = "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein = init_grid(protein)

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

    # run 50 simulated annealing for protein C1
    with open('C4_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Simulated Annealing: " + str(i))

            protein_string = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein = init_grid(protein)

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

if __name__ == '__main__':
	main()
