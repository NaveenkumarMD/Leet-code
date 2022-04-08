class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return 1
        else:
            return n>0 and (n%2==0 and self.isPowerOfTwo(n/2))
        