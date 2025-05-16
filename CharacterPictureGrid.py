def print_grid(grid):
    for row in grid:
        print(''.join(row))

def create_picture():
    grid = [
        [' ', ' ', '*', '*', '*', ' ', ' '],
        [' ', '*', ' ', ' ', ' ', '*', ' '],
        ['*', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', '*'],
        [' ', '*', ' ', ' ', ' ', '*', ' '],
        [' ', ' ', '*', '*', '*', ' ', ' '],
    ]
    return grid

picture = create_picture()
print_grid(picture)
