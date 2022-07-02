def dfsutil(arr,vis,v):
    vis.add(v)
    print(v)
    for i in range(len(arr)):
        if arr[v][i]==1 and i not in vis:
            vis.add(i)
            dfsutil(arr=arr, vis=vis, v=i)
def dfs(arr):
    vis=set()
    dfsutil(arr,vis,0)
arr=[
    [0,1,1,1],
    [1,0,1,1],
    [1,0,0,1],
    [1,1,1,0]
]
dfs(arr)



