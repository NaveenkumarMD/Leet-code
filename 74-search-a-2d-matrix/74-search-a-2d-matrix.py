class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[]
        for i in range(len(matrix)):
            arr.extend(matrix[i])
        start=0
        end=len(arr)-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]==target:
                return True
            if arr[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return False
        