import typing as ty
from functools import reduce

def build_grid_from_list_map(list_map: ty.List[str]) -> ty.List[ty.List]:
    return [list(grid_row) for grid_row in list_map]

def encounters_multipled(encounters: ty.List):
    if len(encounters) == 1:
        return encounters[0]

    return reduce(lambda x, y: x * y, encounters)

def get_encountered_trees(
    tree_map: ty.List, move_x: int, move_y: int) -> int:
    encountered_trees = 0
    current_x = 0
    current_y = 0

    grid = build_grid_from_list_map(tree_map)
    grid_rows = len(grid) - 1
    grid_cols = len(grid[0]) - 1

    out_bound = False

    while True:
        if current_y + move_y > grid_rows:
            break

        current_y += move_y

        if current_x + move_x > grid_cols:
            current_x = (current_x + move_x - grid_cols) - 1
        else:
            current_x += move_x
        
        encounter = grid[current_y][current_x]

        if encounter == '#':
            encountered_trees += 1
            marker = 'X'
        else:
            marker = 'O'

        grid[current_y][current_x] = marker

    return encountered_trees


def move_by_patterns(tree_map: ty.List, movements: ty.List) -> int:
    encounters = list()
    for move in movements:
        encounters.append(
            get_encountered_trees(tree_map, *move)
        )
    return encounters_multipled(encounters)