with open("input.txt", "r", newline="\n") as f:
    file = f.read().splitlines()

# Puzzle 1
tree_grid = []
for line in file:
    tree_grid.append([*line])


def cal_outer_trees(tree_grid: list[list]) -> int:
    """Calculates number of trees around the edge"""
    row_len = len(tree_grid[0]) * 2
    col_len = (len(tree_grid) - 2) * 2
    return row_len + col_len


visible_trees = cal_outer_trees(tree_grid)


def check_greater_equal_to(input: list, val: int) -> int:
    """Checks if any of the values in the input are greater or equal to val"""
    for i in input:
        if i >= val:
            return 1 # not visible
    return 0 # visible


def is_visible(tree_grid: list[list], row: int, col:int ) -> bool:
    """Checks whether tree is visible from ANY side"""
    tree = tree_grid[row][col]
    left_row = tree_grid[row][:col]
    right_row = tree_grid[row][col + 1:]
    top_col = [tree_grid[row_indx][col] for row_indx in range(0, row)]
    bottom_col = [tree_grid[row_indx][col] for row_indx in range(row + 1, len(tree_grid))]
    checks = [left_row, right_row, top_col, bottom_col]
    not_visible_count = 0

    for check in checks:
        not_visible_count += check_greater_equal_to(check, tree)

    if not_visible_count == 4:
        return False
    
    return True


def visible_count(tree_grid: list[list]) -> int:
    """Calculates the number of inner visible trees"""
    num_of_trees = 0
    for row in range(1, len(tree_grid[0]) - 1):
        for col in range(1, len(tree_grid) - 1):
            if is_visible(tree_grid, row, col):
                num_of_trees += 1
    return num_of_trees

visible_trees += visible_count(tree_grid)

print(f"Number of visible trees is {visible_trees}")