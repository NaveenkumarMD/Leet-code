class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr=[
            [0 for i in range(len(grid[0]))] for j in range(len(grid))
        ]
        m=len(grid)
        n=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                i1=((i+(j+k)//n))%m
                j1=(j+k)%n
                arr[i1][j1]=grid[i][j]
        return arr