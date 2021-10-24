def minimumpath(grid):
    col=len(grid[0])
    row=len(grid)
    for i in range(1,col):
        grid[0][i]+=grid[0][i-1]
    for i in range(1,row):
        grid[i][0]+=grid[i-1][0]
    for i in range(1,row):
        for j in range(1,col):
            print(grid[i][j])
            grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
            print(grid[i][j])
    return grid[row-1][col-1]

x=minimumpath([[1,2,3],[4,5,6]])
print(x)