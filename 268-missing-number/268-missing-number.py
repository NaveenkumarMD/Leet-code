class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=len(nums)
        for i in range(x+1):
            if i not in nums:
                return i