GRID_SIZE = 21
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def print_grid(grid):
    for row in grid:
        print(row)


if __name__ == "__main__":
    # init grid
    grid[0] = [1 for _ in range(GRID_SIZE)]
    for i in range(1, GRID_SIZE):
        grid[i][0] = 1

    # solve
    for i in range(1, GRID_SIZE):
        for j in range(1, GRID_SIZE):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    # print_grid(grid)
    print(grid[-1][-1])
