class Solution:
    def firstBadVersion(self, n: int) -> int:
        bot = 0 
        while bot < n: 
            mid = bot + (n-bot)//2
            if isBadVersion(mid): 
                n = mid
            else: 
                bot = mid+1
        return bot