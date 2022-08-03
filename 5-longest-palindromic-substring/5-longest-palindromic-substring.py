class Solution(object): 
    def longestPalindrome(self, s):
        res=""
        for i in range(len(s)):
            start=i
            end=i
            while start>=0 and end<=len(s)-1 and s[start]==s[end]:
                start-=1
                end+=1
            if len(res)<len(s[start+1:end]):
                res=s[start+1:end]
            start=i
            end=i+1
            while start>=0 and end<=len(s)-1 and s[start]==s[end]:
                start-=1
                end+=1
            if len(res)<len(s[start+1:end]):
                res=s[start+1:end]

        return res