
class Info():
    def __init__(self, filepath, protein_input, algorithm, dimension):
        self.filepath = filepath
        self.protein_name = protein_input
        self.algorithm = algorithm
        self.dimension = dimension


    # def generate_filepath():
    #     date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        
    #     filepath = "data\hillclimber\hc_" + str(date) + ".csv"
    #     File.filepath = filepath

    # def generate_header():
    #     with open(File.filepath, 'w', newline='') as csvfile:
    #         datawriter = csv.writer(csvfile)
    #         datawriter.writerow(["# This is a datafile generated for protein: " + str(global_vars.protein.protein_string)])
    #         datawriter.writerow(["# It is generated with a" +  File.algorithm + "algorithm."])
