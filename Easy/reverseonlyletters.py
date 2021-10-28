class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i=0;
        j=len(s)-1
        while(i<j):
            if not s[i].isalpha():
                i+=1
                continue
            if not s[j].isalpha():
                j-=1
                continue
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return "".join(s)


x=Solution()
y=x.reverseOnlyLetters(s = "Test1ng-Leet=code-Q!")
print(y)
