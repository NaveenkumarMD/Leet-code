from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        arr=[]
        i=0
        evenflag=(k%2==0)
        def median(arr):
            arr.sort()
            if not evenflag:
                return float(arr[k//2])
            else:
                return float((arr[k//2]+arr[(k//2)-1] )/2)
        while i<len(nums)-k+1:
            temp=nums[i:i+k]
            arr.append(median(temp))
            i+=1
        return arr



        

x=Solution()
x.medianSlidingWindow(nums = [1,2,3,4,2,3,1,4,2], k = 3)

