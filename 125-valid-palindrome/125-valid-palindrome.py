class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalnum():
                i=i.casefold()
                res+=i
        return res==res[::-1]
        