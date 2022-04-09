class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return 1
        else:
            return n>0 and (n%4==0 and self.isPowerOfFour(n/4))
        