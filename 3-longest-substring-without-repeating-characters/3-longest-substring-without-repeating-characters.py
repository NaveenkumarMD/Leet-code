class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=set()
        res=0
        start=0
        for i in range(len(s)):
            while s[i] in c:
                c.remove(s[start])
                start+=1
            c.add(s[i])
            res=max(i-start+1,res)
        return res
            