class Solution:
    def diagonalSum(self, mat) -> int:
        s1=0
        s2=0
        n=len(mat)-1
        print(n)
        for i in range(len(mat)):
            if i!=n-i:
                s1+=mat[i][n-i]
            s2+=mat[i][i]
        return s1+s2
        