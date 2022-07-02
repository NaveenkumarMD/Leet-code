def dfs(arr,v,vis,temp):
    vis.add(v)
    temp.append(v)
    for i in range(len(arr)):
        if arr[v][i]==1 and i not in vis:
            temp=dfs(arr, i, vis, temp)
    return temp
def components(arr):
    vis=set()
    cc=[]
    for v in range(len(arr)):
        if v not in vis and any([i==1 for i in arr[v]]):
            temp=[]
            cc.append(dfs(arr,v,vis,temp))
    return cc
arr=[
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,1],
    [0,0,1,0]
]
print(components(arr))