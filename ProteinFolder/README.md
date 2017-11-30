# Protein folding algorithms (for folding in 2D)
In this project we try to write algorithms that fold proteins to their most stable configuration. The proteins are solely made of  unspecified hydrophobic (H) and polar (P) amino acids, and Cystein (C). Hydrophobic interactions between H's and sulphur bounds between Cysteins contribute to the stabitity of proteins. 

## Getting Started
Get this program on your computer by downloading the Team50 github repository. 
Uncomment the type of algorithm you want to use in main.py inside the Protein Folder. The program will ask you for an input: this can be A1, B1-B4 or C1-C4 for the proteins specified for our problem. You can find these proteins in assignements.txt in the inputFolder. You can also type your own protein, consisting of H,P and C amino acids.
If you choose the hillclimber algorithm, you can plot the data by adding the function plothillclimber() in the main.py after you've run the hillclimber.

## More about the problem this case is based on
Long strands of Amino Acids make proteins. Proteins are important for many processes in the human body. It is known that proteins in body cells are folded in specific ways. These foldings determine the functioning of the protein. If it's a wrong fold, the proteins can cause many diseases. Therefore it is of great importance for pharmaceutical industry and medical science to be able to say something about the exact form of folding

Some things are known about the mechanism of folding: hydrophobic/polar amino acids (H) 'like' to be side by side. Hydrophylic/apolar amino acids (P) don't have that preferation. If two hydrophobic amino acids lie next to each other, there is some sort of stability by the attractive forces between the two. The more of this stability, te bigger the total stability of the protein. For scientists and pharmacists it is important to know what the maximum stability is a protein can reach.

The goal is of this project is to fold the given proteins so that they are maximally stable. To reach this goal we will make a program that folds a protein in it's most stable configuration. The program takes a protein string as user input. The program folds proteins that are made of only P's and H's. H's are the hydrophobic Amino Acids here and if they are next to eachother, this counts as -1 for stability.

## The Protein Optimization Program
With rotation matrices.

The main file has dependencies on a lot of other files with other functions. Here, the most important ones are explained.

GLOBAL_VARS
Holds all the global variables that are needed in every file: protein_string, grid, coordinates, winning score, current score and the class amino with in it: an ID, the letter (H/P/C), and x,y coordinates

INPUT_STRING
After you run the main file, the input_string function is the first one to be called. It wil ask you for a string input. The assignements we need to are saved in a .txt file. This way you can put in A1,B1,B2,C1, etc. You can also put in a string containing H,P and C. This function calls the init_grid function.

INIT_GRID, UPDATE_GRID
The init_grid function is called once in the whole program. It initializes the grid and the coordinates of the protein string. The update_grid function takes it from there, updating the grid using the coordinates of the amino acids.

FOLD
The fold function takes the ID of the amino that's being folded, and the direction to which it's folded. The aminos from the ID are cleared in the grid. The new coordinates are calculated using a rotation matrix. There's checked if there are no collisions. If there are none, the fold is done. If there are, the fold is made undone and the aminos are putted back in the grid.

SCORE
In the score file a function is implemented that takes the grid from global_vars as input and returns the stability as an integer. It does this by iterating over the protein and distracting 1 (for H) or 5 (for C) from the stability everytime an H (or C) is under or left from another H (or C) and is not bonded.

ALGO_BRUTE_FORCE
This Brute Force algorithm searches trough the whole space state and gives the first protein back that had the best score.

HILLCLIMBER
This hillclimber algorithm does 3 random foldations, and checks for a better stability. Does this 5000 iterations (for now). We are searching for when all the proteins stabilize to make an estimation for the number of iterations.

PLOTS
This dataplotterplots the scores of the protein at each iteration of the last hillclimber program you ran.

## Authors
Christian Bijvoets, David van Grinsven and Natasja Wezel

This program was made in the context of the Minor Programming we followed at the UvA, for the heuristics project november/december 2017.
Case: Protein Powder

