import math
from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minz=math.inf
        maxz=math.inf*-1
        res=-1
        for i in range(len(nums)):
            if nums[i]<=minz:
                minz=nums[i]
                maxz=math.inf*-1
            elif nums[i]>=maxz:
                maxz=nums[i]
                res=max(res,maxz-minz)
        return res
cl=Solution()
s=cl.maximumDifference([1,5,2,10])
print(s)