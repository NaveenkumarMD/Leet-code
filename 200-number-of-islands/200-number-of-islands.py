from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visited=set()
        islands=0
        def bfs(r,c):
            q=deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                r,c=q.popleft()
                directions=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in directions:
                    if (r+dr) in range(rows) and (c+dc) in range(cols) and (r+dr,c+dc) not in visited and  grid[r+dr][c+dc] =="1":
                        q.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    islands+=1
        return islands