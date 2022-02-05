class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax=0
        maxsum=nums[0]
        for i in nums:
            if currmax<0:
                currmax=0
            currmax+=i
            maxsum=max(maxsum,currmax)
        return maxsum
        