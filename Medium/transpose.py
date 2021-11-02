class Solution:
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        print(matrix)

        for arr in matrix:
            i,j=0,len(matrix)-1
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        print(matrix)

x=Solution()
y=x.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])