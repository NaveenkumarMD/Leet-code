class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(t):
            if t[j]==s[i]:
                i+=1
                j+=1
            elif t[j]!=s[i]:
                j+=1
        if i!=len(s):
            return False
        return True