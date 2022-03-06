class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small=prices[0]
        large=0
        for i in prices[1:]:
            if i<small:
                small=i
            if i>large:
                large=max(large,i-small)
        return large