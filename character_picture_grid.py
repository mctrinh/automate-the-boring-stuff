# Define the grid
grid = [['.','.','.','.','.','.'],
        ['.','O','O','.','.','.'],
        ['O','O','O','O','.','.'],
        ['O','O','O','O','O','.'],
        ['.','O','O','O','O','O'],
        ['O','O','O','O','O','.'],
        ['O','O','O','O','.','.'],
        ['.','O','O','.','.','.'],
        ['.','.','.','.','.','.']]

# Print the grid transposed
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()  # Move to the next line after printing each row
