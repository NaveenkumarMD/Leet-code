from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dit=Counter(nums)
        count=0
        for i,j in dit.items():
            if j>1:
                count+=j*(j-1)/2
        return int(count)