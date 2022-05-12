class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a=bin(a)[2:].zfill(32)
        b=bin(b)[2:].zfill(32)
        c=bin(c)[2:].zfill(32)
        res=0
        for i in range(32):
            if c[i]=='1' and a[i]==b[i]=='0': res+=1
            if c[i]=='0':
                if a[i]==b[i]=='1': res+=2
                elif a[i]=='1' or b[i]=='1': res+=1
        return res