# Project Euler Problem 15

n = 20 # size of n by n grid
n += 1
grid = [[0 for i in range(n)] for j in range(n)]

# Insert 1s on top and left side
for i in range(n):
    grid[i][0] += 1
    grid[0][i] += 1
    
grid[0][0] = 1 # Correct double counting grid[0][0]

# Fill in grid - value represents number of paths that pass through point
for i in range(1,n):
    for j in range(1,n):
        grid[i][j] += (grid[i-1][j] + grid[i][j-1])

# Print Ans
print(f'Ans = {grid[n-1][n-1]}')
