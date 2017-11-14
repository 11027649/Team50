# Team50

Minor Programmeren UvA: Programmeertheorie
Heuristieken project november/december 2017
Case: Protein Powder

Programmers: Christian Bijvoets, David van Grinsven and Natasja Wezel

Long strands of Amino Acids make proteins. Proteins are important for many processes in the human body. It is known that proteins in body cells are folded in specific ways. These foldings determine the functioning of the protein. If it's a wrong fold, the proteins can cause many diseases. Therefore it is of great importance for pharmaceutical industry and medical science to be able to say something about the exact form of folding

Some things are known about the mechanism of folding: hydrophobic amino acids 'like' to be side by side. Hydrophylic amino acids don't have that preferation. If two hydrophobic amino acids lie next to each other, there is some sort of stability by the attractive forces between the two. The more of this stability, te bigger the total stability of the protein. For scientists and pharmacists it is important to know what the maximum stability is a protein can reach. 

The goal is of this project is to fold the given proteins so that they are maximally stable. To reach this goal we will make a program that folds a protein in it's most stable configuration. The program takes a protein string as user input.

The program folds proteins that are made of only P (Proline) and H (Histidine). Histidines are the hydrophobic Amino Acids here and if they are next to eachother, this counts as -1 for stability.

The code now allows you to input a protein string. It let's you fold the protein at places you can choose. It also calculates the stability of the protein. Now we are starting to implement algorithms and comparing the scores of the folded proteins to find the protein that is folded the best.
