class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid=board
            #Looping the row 
        for i in range(len(grid)):
            if not self.validate_row(grid,i):
                return False

        #Looping the column
        for j in range(len(grid)):
            if not self.validate_column(grid,j):
                return False

        #Looping the 3*3 box 
        for i in range(0,len(grid),3):
            for j in range(0,len(grid),3):
                if not self.validate_box(grid,i,j):
                    return False
        return True

    # Validating the row
    def validate_row(self,grid,row):
        valid_row = []
        for i in range(len(grid)):
            if grid[row][i]!='.':
                if grid[row][i] in valid_row:
                    return False
                else:
                    valid_row.append(grid[row][i])
        return True

    # Validating the column    
    def validate_column(self,grid,column):
        valid_column = []
        for i in range(len(grid)):
            if grid[i][column]!='.':
                if grid[i][column] in valid_column:
                    return False
                else:
                    valid_column.append(grid[i][column])
        return True

    # Validating the 3*3 matrix values
    def validate_box(self,grid,start_row,end_column):
        valid_box =[]

        for i in range(0,3):
            for j in range(0,3):
                if grid[start_row+i][end_column+j]!='.':
                    box_val = grid[start_row+i][end_column+j]
                    if box_val in valid_box:
                        return False
                    else:
                        valid_box.append(box_val)
        return True