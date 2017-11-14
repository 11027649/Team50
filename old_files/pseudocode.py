
def init_protein():
	de eerste keer dat een amino wordt ingevuld. Vraagt om user input. Returned een grid met
	het protein horizontaal liggend daarin.

def fold_protein(amino_number, pos_next, grid):
	old_grid = grid
	Neemt een oud grid als input, om deze op te slaan en terug te geven als een vouwing niet 
	mogelijk is. 

	Aan de hand van amino_number en pos_next wordt een nieuw grid ingevuld. 

	if vouwing is possible:
	Als dit kan (dus als elke keer dat een nieuw amino erin wordt gezet, daar nog niets staat)
	worden de coordinaten in de Class Amino aangepast.
	return new_grid

	if vouwing is not possible:
	Als dit niet kan wordt het old_grid gereturned. De coordinaten in de class zijn dus niet
	aangepast als dit gebeurt.

def score(grid):
	Aan de hand van het protein in het grid wordt een score bepaald, door elke keer als naast 
	een H een andere H ligt 0.5 van de score af te halen.

	return score

def print_grid(grid):
	Print het grid (zonder streepjes en shit)

def main():

if __name__ == '__main__':
	main()




