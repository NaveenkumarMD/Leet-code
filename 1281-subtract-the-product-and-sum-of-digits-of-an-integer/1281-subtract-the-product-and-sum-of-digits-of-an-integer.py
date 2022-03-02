class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        while n>0:
            p*=n%10
            s+=n%10
            n//=10
        return p-s
        