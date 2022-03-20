class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=0
        maxsum=nums[0]
        for i in nums:
            if currsum<0:
                currsum=0
            currsum+=i
            maxsum=max(currsum,maxsum)
        return maxsum
        