def stitch_t_shape(n, pattern):
    if n < 3 or n > 39 or n % 2 == 0:
        raise ValueError("Grid size must be a positive odd number between 3 and 39 inclusive")
    if len(pattern) < 1 or len(pattern) > 50:
        raise ValueError("Pattern length must be between 1 and 50 inclusive")

    # Create an n by n grid filled with full-stop characters
    grid = [['.' for _ in range(n)] for _ in range(n)]

    # Fill the top row of the T
    for i in range(n):
        grid[0][i] = pattern[i % len(pattern)]

    # Fill the middle column of the T
    middle_col = n // 2
    for i in range(1, n):
        grid[i][middle_col] = pattern[(n + i - 1) % len(pattern)]

    # Print the grid
    for row in grid:
        print(''.join(row))

# Example usage
n = int(input())
pattern = input()
stitch_t_shape(n, pattern)