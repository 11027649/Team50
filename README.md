Kunnen jullie voor de punten aanvraag de github map van 10:44 (de tijd dat we het (tweede) mailtje stuurden) gebruiken...

Usage: In folder "theWAY" run main.py, uncomment the type of algorithm you want to use. To plot the data of the last hillclimber result, use plotdata.py.

# Team50

Minor Programmeren UvA: Programmeertheorie

Heuristieken project november/december 2017

Case: Protein Powder


Programmers: Christian Bijvoets, David van Grinsven and Natasja Wezel

Long strands of Amino Acids make proteins. Proteins are important for many processes in the human body. It is known that proteins in body cells are folded in specific ways. These foldings determine the functioning of the protein. If it's a wrong fold, the proteins can cause many diseases. Therefore it is of great importance for pharmaceutical industry and medical science to be able to say something about the exact form of folding

Some things are known about the mechanism of folding: hydrophobic/polar amino acids (H) 'like' to be side by side. Hydrophylic/apolar amino acids (P) don't have that preferation. If two hydrophobic amino acids lie next to each other, there is some sort of stability by the attractive forces between the two. The more of this stability, te bigger the total stability of the protein. For scientists and pharmacists it is important to know what the maximum stability is a protein can reach.

The goal is of this project is to fold the given proteins so that they are maximally stable. To reach this goal we will make a program that folds a protein in it's most stable configuration. The program takes a protein string as user input. The program folds proteins that are made of only P's and H's. H's are the hydrophobic Amino Acids here and if they are next to eachother, this counts as -1 for stability.

# "Protein Optimization Program"
With rotation matrices.

To use the program you only need to run one file: main.py in the "theWAY" folder. Uncomment the type of algorithm you want to use in the main file. This file has dependencies on 11 other files: message, input_string, init_grid, update_grid, print_protein, fold, score, global_vars, algo_brute_force, hillclimber, plotdata.

To plot the data from the last hillclimber you used, run: plotdata.py.

GLOBAL_VARS
Holds all the global variables that are needed in every file: protein_string, grid, coordinates, winning score, current score and the class amino with in it: an ID, the letter (H/P/C), and x,y coordinates

MESSAGE
Enables you to print a nice message to the screen. This is used for debugging, but we want to use it later on for a nice UI.

INPUT_STRING
After you run the main file, the input_string function is the first one to be called. It wil ask you for a string input. The assignements we need to are saved in a .txt file. This way you can put in A1,B1,B2,C1, etc. You can also put in a string containing H,P and C. This function calls the init_grid function.

INIT_GRID
The init_grid function is called once in the whole program. It initializes the grid and the coordinates of the protein string.

PRINT_PROTEIN
Prints the protein.

FOLD
This is where the magic happens :-). The fold function takes the ID of the amino that's being folded, and the direction to which it's folded. The aminos from the ID are cleared in the grid. The new coordinates are calculated using a rotation matrix. There's checked if there are no collisions. If there are none, the fold is done. If there are, the fold is made undone and the aminos are putted back in the grid.

SCORE
The score function works the same as the in the alternative way, except that it uses the grid and protein from the global_vars file and doesn't return things but puts them in the global_vars.

ALGO_BRUTE_FORCE
This Brute Force algorithm searches trough the whole space state and gives the first protein back that had the best score.

HILLCLIMBER
This hillclimber algorithm does 3 random foldations, and checks for a better stability. Does this 1000 iterations (for now). We are searching for when all the proteins stabilize to make an estimation for the number of iterations.

PLOTDATA
This dataplotter, which you can run by typing 'python plotdata.py' plots the last scores at each iteration of the last hillclimber program you ran.


# "Old data structure"
Maybe we just delete this later on, but not yet.

To use the program you only need to run one file: main.py. This file has dependencies on 4 other files: initialize, folder, score, animation, amino, and helper_prints.

INITIALIZE

FOLDER

SCORE
In the score file a function is implemented that takes a grid as input and returns the stability as an integer. It does this by iterating over the grid and distracting 0.5 from the stability everytime an H is above, under, left or right from another H. Than it adds 1 for each 'real' bond.

ANIMATION
In the animation file two functions are implemented: one to print the protein in a nice way, and one to clear the screen and to wait a little to make a real animation. This way you can choose: do you want to see all different folded proteins beneath eachother, or do you want to see an animation of the folding process.

AMINO
The amino file only contains the class Amino. In Amino there are saved some variables: the letter (P or H), the position of the next Amino (which can be L, R, or C), the coordinates of the Amino and the direction (which can be 0 (up), 1 (right), 2 (down) or 3 (up)).

HELPER_PRINTS
The helper prints file contains two print functions: print_coordinates to print all of the coordinates of all Amino Acids (mainly used for debugging) and print_protein to print the protein (really plain, without bonds etc.).
