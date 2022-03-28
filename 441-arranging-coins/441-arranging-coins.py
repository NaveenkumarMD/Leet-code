class Solution:
    def arrangeCoins(self, n: int) -> int:
        def getsum(n):
            return (n*(n+1))//2
        curr=1
        while getsum(curr)<=n:
            curr+=1
        return curr-1
        