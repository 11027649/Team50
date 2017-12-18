![team50-logo](https://github.com/Segouta/Team50/blob/master/doc/logoBanner.png)

# Protein folding algorithms
This project uses algorithms to fold proteins (with certain given limitations such as angles) into their most stable configuration. The proteins are solely built up out of unspecified hydrophobic (H) and polar (P) amino acids, and Cystein (C). Hydrophobic interactions between H's and sulphur bounds between Cysteins contribute to the stabitity of proteins. 

## Getting Started
Get this program on your computer by downloading the Team50 github repository. 
Install the requirements by running **pip install -r requirements.txt** in your terminal.
Use the main program by running **python main.py** in your terminal
The program will ask you 2 things: 
- The protein that you want to fold.
- The dimension you want to fold in.
- The algorithm you want to use to do so.
You can enter your preferations by typing the number that matches with the wanted option and hitting enter.
The proteins you can enter can be A1, B1-B4 or C1-C4 for the proteins specified for our problemset. You can find these proteins in assignements.txt in the inputFolder. You can also type your own protein, consisting of H, P and C amino acids.

## More about the problem this case is based on
Long strands of Amino Acids make proteins. Proteins are important for many processes in the human body. It is known that proteins in body cells are folded in specific ways. These foldings determine the functioning of the protein. If there is a wrong fold, the proteins can cause many diseases. Therefore it is of great importance for pharmaceutical industry and medical science to be able to say something about the exact form of folding.

Some things are known about the mechanism of folding: hydrophobic/polar amino acids (H) 'like' to be side by side. Hydrophylic/apolar amino acids (P) don't have that preferation. If two hydrophobic amino acids lie next to each other, there is some sort of stability by the attractive forces between the two. The more of this "bonds", the bigger the total stability of the protein will be. For scientists and pharmacists it is important to know what the maximum stability is a protein can reach.

The goal is of this project is to fold the given proteins so that they are maximally stable. To reach this goal we have written a program that folds a protein into it's most stable configuration. The program takes a protein string as user input. If two H's are next to each other, the protein becomes more stable with a score of -1. If two C's are next to each other, the stability is decreased even more, with a change of -5. **A lower score is better!**

## Results
The best stabilities for all the proteins are represented in the table below. The scores for A1 and B1 are certain, because these are calculated by a brute force algorithm. The other stabilities are approached by other algorithms (see below) and are uncertain.



## Algorithms ##

There are 7 algorithms ready to be used. In this sections, a brief elaboration is provided on each of them. An important note: 2d and 3d are working for all of these algorithms, and if 2d is selected, the 3d options are not considered optional. So it's not doing the 3d options but neglecting them, its just not doing the 3d options, because the extra folds would be a waste of runtime.
In various algorithms, the number 14 pops up. This is not a random value, it is determined running a protein using a parameterization for different amount of folds per iteration. The result was that the range was much wider using values around 14, with 14 as the best option. We therefore decided to stick to 14.

**Brute Force**

This algorithm uses the depth first principle to iterate through the state space of the options of the protein that need to be solved. It however keeps track of rotational duplicates, and in the way we implemented the first two amino acids, the mirrored options are also pruned out. So this brute force traverses the smallest state space possible. 

**Hill Climber**

This hillclimber does 14 random folds per iteration. These folds may be invalid, so it might just fold less then 14 folds netto. After the 14 attempts, it checks if the configuration of the protein is in a better score then before the 14 folds. If so, it takes this new configuration as the starting point for the next iteration. If it however doesn't find a better score, it starts the next iteration with the same configuration as before.

**Fold Control Hillclimber**

This hillclimber resembles the normal hill climber a bit. The big difference is that the Fold Control checks after eacht of the 14 folds if an improvement is found. If such an improvement is found, the iteration stops.

**Extend Fold Hillclimber**

This hillclimber is a bit different than the other hillclimbers. It starts with iterations with only 2 folds per iteration. If it does not find some improvement within 1000 iterations, it extends it's folding range per iteration i.e. it folds 3 times per iteration. For the rest, it's just doing 14 folds and does not wait till there were 14 succesfull folds like Fold Control Hillclimber. If it does not find a better value when its extended all the way up to 100 folds per iteration, the algorithm is stopped.

**Simulated Annealing**

This algorithm is based on the same 14-random-folds-technique as the hillclimbers. The big difference is that this algorithm uses a cooling scheme. It "cools" from 1 to 0 degrees linearly through the iterations. The closer it is to 0, the smaller the chance that a deterioration will be accepted. So when further in the progress, the algorithm will gradually stop accepting worse configurations.

**Simulated Annealing Control**

This algorithm is the same as the previous algorithm, it just stops the iteration immediately once an improvement is found, just like in Fold Control Hillclimber. It has the same cooling scheme as the previous algorithm.

**Simulated Annealing Reheat**

This algorithm is based on the same principle as the normal simulated annealing algorithm, it just reheats half way. So it cools down from 1 to 0 in half of the total iterations, then is set back to 1 and cooled down again.

## The Protein Optimization Program
The main file has dependencies on a lot of other files with other functions. Here, the most important ones are explained.

**classes**

There are two classes: *protein*, and *run_info*. In *run_info* all the info for this run is stored, this is information like, what protein string, what algorithm and in which dimension (2D or 3D.)
Protein holds the coordinates of each amino acid, the protein string, and the grid.

**input_string**

After you run the main file, the input_string function is the first one to be called. It wil ask you for a string input. The assignements we need to are saved in a .txt file. This way you can put in A1,B1,B2,C1, etc. You can also put in a string containing H,P and C. This function calls the init_grid function.

**init_grid, update_grid**

The init_grid function is called once in the whole program. It initializes the grid and the coordinates of the protein string. The update_grid function takes it from there, updating the grid using the coordinates of the amino acids.

**fold**

The fold function takes the ID of the amino that's being folded, and the direction to which it's folded. The aminos from the ID are cleared in the grid. The new coordinates are calculated using a rotation matrix. There's checked if there are no collisions. If there are none, the fold is done. If there are, the fold is made undone and the aminos are putted back in the grid.

**score**

In the score file a function is implemented that takes the grid from global_vars as input and returns the stability as an integer. It does this by iterating over the protein and distracting 1 (for H) or 5 (for C) from the stability everytime an H (or C) is under or left from another H (or C) and is not bonded.

**algorithms**

The Brute Force algorithm searches trough the whole space state and gives the first protein back that had the best score.
The hillclimber algorithm does 14 random foldations and checks for a better stability. Does this 5000 iterations.
The Simulated Annealing algorithm does 14 random foldations and checks for a better stability, but it also calculates an acceptance chance for a detoriation.

**plots**

Plots the scores of the protein at each iteration of the last hillclimber or simulated annealing program you ran.
Also plots the best protein after you ran an algorithm.

## Libraries
The libraries used during the progress of making - or currenty in - the program were the following:
colorama 0.3.9
cycler 0.10.0
matplotlib 2.1.0
numpy 1.13.3
pygame 1.9.3
pyparsing 2.2.0
python-dateutil 2.6.1
pytz 2017.3
six 1.11.0
termcolor 1.1.0


## Authors
Christian Bijvoets, David van Grinsven and Natasja Wezel

This program was made in the context of the Minor Programming we followed at the UvA, for the heuristics project november/december 2017.
[Case: Protein Powder](http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er)
