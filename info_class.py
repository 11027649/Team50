import datetime
import csv

class Info():
    def __init__(self, filepath, protein_input, algorithm, dimension):
        self.filepath = filepath
        self.protein_name = protein_input
        self.algorithm = algorithm
        self.dimension = dimension


    def generate_filepath(self, algorithm_short):
        date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        
        route = "data\hillclimber\\" + algorithm_short + str(date) + ".csv"
        self.filepath = route

    def generate_header(self, protein_string):
        dimension = '3D'
        
        if self.dimension == 0:
            dimension = '2D'

        with open(self.filepath, 'w', newline='') as csvfile:
            datawriter = csv.writer(csvfile)
            datawriter.writerow(["# This is a datafile generated for protein: " + str(protein_string)])
            datawriter.writerow(["# It is generated with a " +  self.algorithm + " algorithm."])
            datawriter.writerow(["# The protein is folded in: " + dimension])
