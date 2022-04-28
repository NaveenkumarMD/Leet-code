class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set(candyType)
        x=len(candyType)
        return x//2 if (len(s)>=x//2) else len(s)
        