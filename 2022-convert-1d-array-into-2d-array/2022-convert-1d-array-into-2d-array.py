class Solution:
    def construct2DArray(self, original,m,n):
        N=len(original)
        if N!=m*n:
            return []
        j=0
        arr=[]
        temp=[]
        for i in range(N):
            if j<n:
                temp.append(original[i])
                j+=1
                if  j==n:
                    arr.append(temp)
                    temp=[]
                    j=0
        return arr