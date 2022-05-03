from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        x=Counter(nums)
        s=0
        for i in x:
            if x[i]==1:
                s+=i
        return s
        