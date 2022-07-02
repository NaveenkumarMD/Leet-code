def dfsutil(arr,vis,path,src,dest):
    vis.add(src)
    path.append(src)
    if src==dest:
        print(path)
    else:
        for i in range(len(arr)):
            if i not in vis:
                dfsutil(arr, vis, path, i, dest)
    path.pop()
    vis.remove(src)
        
def findpaths(arr):
    vis=set()
    path=[]
    dfsutil(arr,vis,path,0,3)

arr=[
    [0,1,1,1],
    [1,0,1,1],
    [1,0,0,1],
    [1,1,1,0]
]
findpaths(arr)