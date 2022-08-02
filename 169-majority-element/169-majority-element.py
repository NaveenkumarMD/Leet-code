class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        dit=Counter(nums)
        for i in dit:
            if dit[i]>(len(nums)//2):
                return i
        