class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        x=[[0]*len(grid) for k in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x[i][j]=grid[j][i]
        count=0
        print(x)
        for i in range(len(grid)):
            for j in range(len(x)):
                if x[j]==grid[i]:
                    count+=1
        return count
        