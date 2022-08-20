class Solution:
    def smallestNumber(self, pattern: str) -> str:
        start=-1
        s=[str(i+1) for i in range(len(pattern)+1)]
        for i in range(len(pattern)):
            if pattern[i]=="I":
                start=i
            else:
                j=i
                while j>start:
                    s[j+1],s[j]=s[j],s[j+1]
                    j-=1                
                    
        return "".join(s)