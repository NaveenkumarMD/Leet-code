class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        rottencount=0
        freshcount=0
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                    rottencount+=1
                if grid[i][j]==1:
                    freshcount+=1
        time=0
        def check(x,y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] !=1:
                return False
            return True
        while q and freshcount>0:
            for i in range(len(q)):
                x,y=q.pop(0)
                for dr,dc in directions:
                    dr,dc=x+dr,y+dc
                    if check(dr,dc):
                        q.append((dr,dc))
                        grid[dr][dc]=2
                        freshcount-=1
            time+=1
        print(freshcount)
        if freshcount==0:
            return time
        return -1                