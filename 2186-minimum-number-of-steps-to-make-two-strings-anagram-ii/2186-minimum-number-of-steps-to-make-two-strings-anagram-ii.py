
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dit1=Counter(s)
        dit2=Counter(t)
        count=0
        for i in dit1.keys():
            if i not in dit2:
                count+=dit1[i]
            else:
                if dit1[i]<dit2[i]:
                    count+=dit2[i]-dit1[i]
        for i in dit2.keys():
            if i not in dit1:
                count+=dit2[i]
            else:
                if dit2[i]<dit1[i]:
                    count+=dit1[i]-dit2[i]
        return count
        
                