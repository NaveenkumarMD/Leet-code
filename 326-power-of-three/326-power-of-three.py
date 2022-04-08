class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return 1
        else:
            return n>0 and (n%3==0 and self.isPowerOfThree(n/3))
        