class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0]*n for i in range(n)]
        count=1
        top=0
        bottom=n-1
        left=0
        right=n-1
        while True:
            if left>right:
                break
            for i in range(left,right+1):
                mat[top][i]=count
                count+=1
            top+=1
            if top>bottom:
                break
            for i in range(top,bottom+1):
                mat[i][right]=count
                count+=1
            right-=1
            if left>right:
                break
            for i in range(right,left-1,-1):
                mat[bottom][i]=count
                count+=1
            bottom-=1
            if top>bottom:
                break
            for i in range(bottom,top-1,-1):
                mat[i][left]=count
                count+=1
            left+=1
            if left>right:
                break
        return mat