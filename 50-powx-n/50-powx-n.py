class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper (x,n):
            if n == 0 : return 1
            if x == 0 : return 0
            if x == 1: return 1                
            res = helper(x, n//2)
            
            # odd or even power : example 2^11 = 2*2^5*2^5
            return x*res*res if n%2 else res*res
        res = helper(x,abs(n))
        return res if n>=0 else 1/(res)