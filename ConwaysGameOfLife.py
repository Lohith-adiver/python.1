
print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")
import random
import time
import os

WIDTH = 20
HEIGHT = 10
GENERATIONS = 3


def create_grid():
    return [[random.choice([' ', '█']) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_grid(grid, generation):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Generation {generation}")
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
    for generation in range(1, GENERATIONS + 1):
        print_grid(grid, generation)
        grid = next_generation(grid)
        time.sleep(0.5)
    print("\nSimulation completed after 3 generations.")
except KeyboardInterrupt:
    print("\nSimulation interrupted.")
