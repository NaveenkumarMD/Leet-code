from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minx=min(nums)
        res=0
        for i in nums:
            res+=i-minx
        return res