import random
import time
import os

WIDTH = 20
HEIGHT = 10

def create_grid():
    return [[random.choice([' ', '█']) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(row))

def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
            if grid[nx][ny] == '█':
                count += 1
    return count

def next_generation(grid):
    new_grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == '█':
                if neighbors in [2, 3]:
                    new_grid[i][j] = '█'
            else:
                if neighbors == 3:
                    new_grid[i][j] = '█'
    return new_grid

grid = create_grid()

try:
    while True:
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nSimulation ended.")
