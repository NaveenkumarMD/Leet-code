class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        i=len(s)-1
        res=""        
        while i>=0:
            if s[i]!="#":
                res+=chr(96+int(s[i]))
                i-=1
            else:
                res+=chr(96+int(s[i-2]+s[i-1]))
                i-=3
        return res[::-1]
        