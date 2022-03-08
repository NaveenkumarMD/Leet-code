from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
    
        dit=Counter(s)
        x=-99
        for i,j in dit.items():
            if j==1:
                x=i
                break
        if x==-99:
            return -1
        return s.index(x)