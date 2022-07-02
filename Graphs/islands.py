def dfs(arr,i,j,row,col):
    if i<0 or i>=row or j<0 or j>=col or arr[i][j]==0:
        return
    arr[i][j]=0
    dfs(arr, i+1, j, row, col)
    dfs(arr, i-1, j, row, col)
    dfs(arr, i, j-1, row, col)
    dfs(arr,i, j+1, row, col)
def getislands(arr):
    row=len(arr)
    col=len(arr[0])
    ans=0
    for i in range(row):
        for j in range(col):
            if arr[i][j]==1:
                ans+=1
                dfs(arr, i, j, row, col)
    return ans
            

arr=[
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]
x=getislands(arr)
print(x)