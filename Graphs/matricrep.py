from collections import deque
def bfs(arr):
    vis=set()
    q=deque()
    q.append(0)
    while q :
        curr=q.popleft()
        vis.add(curr)
        print(curr,end=" ")
        for i in range(len(arr)):
            if arr[curr][i]==1 and i not in vis:
                vis.add(i)
                q.append(i) 


arr=[
    [0,1,1,1],
    [1,0,1,1],
    [1,0,0,1],
    [1,1,1,0]
]
bfs(arr)