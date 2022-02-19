class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx=max(nums)
        m=mx//2
        l=[i for i in range(m+1,mx)]
        for i in l:
            if i in nums:
                return -1
        return nums.index(mx)
        