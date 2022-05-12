from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=Counter(nums)
        for i,j in x.items():
            if j==1:
                return i
        