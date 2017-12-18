# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is part of the protein folding program made by Team50.
#
# It contains the class info. Here you can save some variables for later use
# about this particular run.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import datetime
import csv

class Info():
    def __init__(self, filepath, protein_input, algorithm, dimension):
        self.filepath = filepath
        self.protein_name = protein_input
        self.algorithm = algorithm
        self.dimension = dimension


    def generate_filepath(self, algorithm_short):
        """ Generates a filepath for the file that will be used to save de data
            of this run. This is needed to acces the filepath later on, when the
            data has to be plotted. """

        # give the file a name with the year, month, day, hours and minuts of this moment
        date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        route = ""

        # save the data in the right folder
        if algorithm_short.startswith('sa'):
            route = "data\simulated_annealing\\" + algorithm_short + str(date) + ".csv"
        else:
            route = "data\hillclimber\\" + algorithm_short + str(date) + ".csv"
        
        # save the filepath
        self.filepath = route

    def generate_header(self, protein_string):
        """ Generates a short header for the csvfiles. """

        dimension = '3D'
        
        if self.dimension == 0:
            dimension = '2D'
            
        with open(self.filepath, 'w', newline='') as csvfile:
            datawriter = csv.writer(csvfile)
            datawriter.writerow(["# This is a datafile generated for protein: " + str(protein_string)])
            datawriter.writerow(["# It is generated with a " +  self.algorithm + " algorithm."])
            datawriter.writerow(["# The protein is folded in: " + dimension])
