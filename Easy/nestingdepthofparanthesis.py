class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth=0
        count=0
        for i in s:
            if i=="(":
                count+=1
            if i==")":
                count-=1
            if count>maxdepth:
                maxdepth=count
        return maxdepth
                
        
c=Solution()
x=c.maxDepth("(1+(2*3)+((8)/4))+1")
print(x)