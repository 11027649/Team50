# Team50

Minor Programmeren UvA: Programmeertheorie

Heuristieken project november/december 2017

Case: Protein Powder


Programmers: Christian Bijvoets, David van Grinsven and Natasja Wezel

Long strands of Amino Acids make proteins. Proteins are important for many processes in the human body. It is known that proteins in body cells are folded in specific ways. These foldings determine the functioning of the protein. If it's a wrong fold, the proteins can cause many diseases. Therefore it is of great importance for pharmaceutical industry and medical science to be able to say something about the exact form of folding

Some things are known about the mechanism of folding: hydrophobic/polar amino acids (H) 'like' to be side by side. Hydrophylic/apolar amino acids (P) don't have that preferation. If two hydrophobic amino acids lie next to each other, there is some sort of stability by the attractive forces between the two. The more of this stability, te bigger the total stability of the protein. For scientists and pharmacists it is important to know what the maximum stability is a protein can reach. 

The goal is of this project is to fold the given proteins so that they are maximally stable. To reach this goal we will make a program that folds a protein in it's most stable configuration. The program takes a protein string as user input. The program folds proteins that are made of only P's and H's. H's are the hydrophobic Amino Acids here and if they are next to eachother, this counts as -1 for stability.

To use the program you only need to run one file: protein_current.py. This file has dependencies on 4 other files: score, animation, amino, and helper_prints. 

SCORE
In the score file a function is implemented that takes a grid as input and returns the stability as an integer. It does this by iterating over the grid and distracting 0.5 from the stability everytime an H is above, under, left or right from another H. Than it adds 1 for each 'real' bond. 

ANIMATION
In the animation file two functions are implemented: one to print the protein in a nice way, and one to clear the screen and to wait a little to make a real animation. This way you can choose: do you want to see all different folded proteins beneath eachother, or do you want to see an animation of the folding process.

AMINO
The amino file only contains the class Amino. In Amino there are saved some variables: the letter (P or H), the position of the next Amino (which can be L, R, or C), the coordinates of the Amino and the direction (which can be 0 (up), 1 (right), 2 (down) or 3 (up)).

HELPER_PRINTS
The helper prints file contains two print functions: print_coordinates to print all of the coordinates of all Amino Acids (mainly used for debugging) and print_protein to print the protein (really plain, without bonds etc.).

