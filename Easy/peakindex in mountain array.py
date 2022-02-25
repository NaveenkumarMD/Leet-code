from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #using binary search
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right-left)// 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid-1
        return left
x=Solution()
print(x.peakIndexInMountainArray([0,1,3,4,5,6,0]))
                            