print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")
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
