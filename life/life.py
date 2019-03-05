"""Game of life; see test for spec."""


def live(grid):
    new_gen = []
    for floor in grid:
        new_floor = ''
        for index, cell in enumerate(floor):
            if on_the_edge(index, floor):
                new_floor += '.'
            else:
                new_floor += cell
        new_gen.append(new_floor)
    return new_gen


def live_neighbors(grid, row, col) -> int:
    #return 1 if grid[row][col+1] == '*' else 0
    live_cells = 0
    for line in grid:
        for cell in line:
            if cell == '*':
                live_cells += 1
    return live_cells


def on_the_edge(index, floor):
    return index == 0 or index == len(floor) - 1
