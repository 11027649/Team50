from update_grid import update_grid
from global_vars import amino

import global_vars
global_vars.init()

def score():

    score = 0

    grid = global_vars.grid
    coordinates = global_vars.coordinates

    width = len(grid)
    height = len(grid[0])

    for i in range(len(global_vars.protein_string)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        cur_id = grid[x][y].num_id
        if grid[x][y].letter == "H":
            if x > 0 and str(type(grid[x - 1][y])) == "<class 'global_vars.amino'>" and grid[x - 1][y].letter == "H" and abs(cur_id - grid[x - 1][y].num_id) > 1:
                score -= 0.5
            if x < width - 1 and str(type(grid[x + 1][y])) == "<class 'global_vars.amino'>" and grid[x + 1][y].letter == "H" and abs(cur_id - grid[x + 1][y].num_id) > 1:
                score -= 0.5
            if y > 0 and str(type(grid[x][y - 1])) == "<class 'global_vars.amino'>" and grid[x][y - 1].letter == "H" and abs(cur_id - grid[x][y - 1].num_id) > 1:
                score -= 0.5
            if y < height - 1 and str(type(grid[x][y + 1])) == "<class 'global_vars.amino'>" and grid[x][y + 1].letter == "H" and abs(cur_id - grid[x][y + 1].num_id) > 1:
                score -= 0.5

    return score
