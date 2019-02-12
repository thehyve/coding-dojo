"""Game of life; see test for spec."""

def live(grid):
    new_gen = []
    for floor in grid:
        new_floor = ''
        for index, neighbor in enumerate(floor):
            if on_the_edge(index, floor):
                new_floor += '.'
            else:
                new_floor += '*'
        new_gen.append(new_floor)
    return new_gen

def on_the_edge(index, floor):
    return index == 0 or index == len(floor) - 1
