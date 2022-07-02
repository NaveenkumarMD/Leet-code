class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat=matrix
        self.temp=[([0]*(len(matrix[0])+1)) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.temp[i][j+1]=self.temp[i][j]+matrix[i][j]
        print(self.temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum=0
        for row in range(row1,row2+1):
            sum+=self.temp[row][col2+1]-self.temp[row][col1]
        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)