class Solution:
    def minimumMoves(self, s: str) -> int:
        i=0
        n=len(s)
        res=0
        while i<n:
            if s[i]=='x':
                res+=1
                i+=3
            else:
                i+=1
        return res

        

x=Solution()
y=x.minimumMoves("oxox")
print(y)