class Solution:
    def reverseBits(self, n: int) -> int:
        rev=0
        i=0
        while n>0 or i<32:
            i+=1
            rev=rev<<1
            if n&1==1:
                rev^=1
            n=n>>1
        return rev
        