# save position of each amino acid to remember which ones are linked
# dit is een comment
class Amino():
    def __init__(self, letter, pos_next):
        self.letter = letter
        self.pos_next = pos_next


def make_grid():

    # columns
    for i in range(y):

        # rows
        for j in range(x):

            if not isinstance(grid[i][j], str):
                if grid[i][j].letter == 'H' or grid[i][j].letter == 'P':
                    temp = grid[i][j].pos_next
                    if temp == 'U':
                        grid[i-1][j] = '| '
                    elif temp == 'D':
                        grid[i+1][j] = '| '
                    elif temp == 'R':
                        grid[i][j+1] = '---'
                    elif temp == 'L':
                        grid[i][j-1] = '---'


# print the grid: x and y, fill with - and with the protein somewhere in the middle
def print_grid():

    # print columns
    for i in range(y):

        # print rows
        for j in range(x):

            # niet roosterpunten
            if grid[i][j] == ' ':
                if i % 2 == 0 and j % 2 == 0:
                    print('- ', end='')
                else:
                    print('  ', end='')

            # ifinstance (object, classinfo) if object in classinfo, returns True
            elif isinstance(grid[i][j], str):
                print(grid[i][j], end='')

            else:

                # print H blue
                if grid[i][j].letter == 'H':
                    print(grid[i][j].letter, end="")

                # print P red
                elif grid[i][j].letter == 'P':
                    print(grid[i][j].letter, end="")

                # if there's a str next, print a space
                if isinstance(grid[i][j+2], str):
                    print(' ', end='')

        # print an enter
        print()

# initiatie grid, fill with 0
x, y = 29, 29
grid = [[' ' for p in range(x)] for q in range(y)]

# ask user for protein string as input, max length
protein_string = input("Insert protein string: ")

# check if protein isn't too long
if len(protein_string) > 10:
    print("Protein too large...")
    exit(1)

# check if only P and H amino acids are given
for letter in protein_string:
    if (letter.upper() != 'P' and letter.upper() != 'H'):
        print("Please only insert P's and H's...")
        exit(1)

start_x = 3
start_y = 7

# initialize the grid
def initialize_grid():
    """ AFter first user input, initialize the grid with the protein unfolded. """

    for i in range(len(protein_string)):

        if i == len(protein_string) - 1:
            grid[start_y*2][(i+start_x)*2] = Amino(protein_string[i].upper(), 'E')
        else:
            grid[start_y*2][(i+start_x)*2] = Amino(protein_string[i].upper(), 'R')

        # grid[6][6] = Amino('P', 'D')
        # grid[8][6] = Amino('H', 'D')
        # grid[10][6] = Amino('H', 'R')
        # grid[10][8] = Amino('P', 'R')
        # grid[10][10] = Amino('H', 'R')
        # grid[10][12] = Amino('P', 'U')
        # grid[8][12] = Amino('H', 'U')
        # grid[6][12] = Amino('P', 'L')
        # grid[6][10] = Amino('H', 'U')
        # grid[4][10] = Amino('P', 'R')
        # grid[4][12] = Amino('H', 'E')

initialize_grid()
make_grid()
print_grid()
