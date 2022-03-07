class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        mainset=set([i+1 for i in range(len(matrix))])
        for i in range(n):
            x=[matrix[i][j] for j in range(n)]
            y=[matrix[j][i] for j in range(n)]
            for i in mainset:
                if i not in x or i not in y:
                    return False
        return True
                
            