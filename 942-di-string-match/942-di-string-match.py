class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start=-1
        pattern=s
        s=[str(i) for i in range(len(pattern)+1)]
        for i in range(len(pattern)):
            if pattern[i]=="I":
                start=i
            else:
                j=i
                while j>start:
                    s[j+1],s[j]=s[j],s[j+1]
                    j-=1                
                    
        return s