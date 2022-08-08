class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def issafe(board,x,y):
            for i in range(y):
                if board[x][i]=="Q":
                    return False
            i=x
            j=y
            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            i=x
            j=y
            while j>=0 and i<n:
                if board[i][j]=="Q":
                    return False
                i+=1
                j-=1
            return True
        result=[]
        def dfs(board,col):
            if col==n:          
                s=[]
                for i in board:
                    s.append("".join(i))
                result.append(s)
                return True
            res=False
            for i in range(n):
                if issafe(board,i,col):
                    board[i][col]="Q"
                    res=dfs(board,col+1) or res
                    board[i][col]="."
        board=[['.']*n for i in range(n)]
        dfs(board,0)
        return  result

                    
                
            