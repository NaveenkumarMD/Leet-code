class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<3:
            return list(set(nums))[-1]
        else:
            x=list(set(nums))
            x.sort()
            return x[-3] if len(x)>=3 else x[-1]