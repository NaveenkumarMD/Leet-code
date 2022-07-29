from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        dit=defaultdict(lambda:0)
        x=0
        for i in s[:3]:
            if dit[i]==0:
                x+=1
                dit[i]=1
            else:
                dit[i]+=1
        if x==3:
            count+=1
        for i in range(1,len(s)-3+1):
            c=s[i-1]
            d=s[i+3-1]
            dit[c]-=1
            if dit[c]==0:
                x-=1
            if dit[d]==0:
                x+=1
            dit[d]+=1
            if x==3:count+=1
        return count
                
                
            
                
                
            