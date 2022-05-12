class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res=0
        s=0
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                s=i
            res=max(res,i-s+1)
        return res
                
        