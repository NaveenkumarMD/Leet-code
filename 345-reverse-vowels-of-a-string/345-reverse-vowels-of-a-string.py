class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j=0,len(s)-1
        s=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        while i<=j:
            x,y=s[i],s[j]
            if x in vowels and y in vowels:
                s[i],s[j]=y,x
                i+=1
                j-=1
            elif x in vowels and y not in vowels:
                j-=1
            elif y in vowels and x not in vowels:
                i+=1
            else:
                i+=1
                j-=1
        return "".join(s)
                