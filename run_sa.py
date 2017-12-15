from visualization.message import message

from utility.input_string import input_string

from protein_class import Protein

# import algorithms
from algorithms.hillclimber_without import hillclimber
from algorithms.simulated_annealing_without import simulated_annealing

import csv

def main():

    # run 50 simulated annealing for protein C1
    with open('B1_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("SA: " + str(i))

            protein_string = "HHPHHHPHPHHHPH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

    # run 50 simulated annealing for protein C1
    with open('B2_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("SA: " + str(i))

            protein_string = "HPHPPHHPHPPHPHHPPHPH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

    # run 50 simulated annealing for protein C1
    with open('B3_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("SA: " + str(i))

            protein_string = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

    # run 50 simulated annealing for protein C1
    with open('B4_3D_SA.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("SA: " + str(i))

            protein_string = "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()

            protein = simulated_annealing(protein)
            
            datawriter.writerow([i] + [protein.winning_score])

if __name__ == '__main__':
	main()
