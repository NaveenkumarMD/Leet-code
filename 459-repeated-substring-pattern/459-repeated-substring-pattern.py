class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)==0:
            return False
        for i in range(1,(len(s)//2)+1):
            temp=s[:i]

            l=len(s)//i
            print(l)
            if temp*l==s:
                return True
        return False