from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        x=Counter(s)
        for i,j in x.items():
            if j==1:
                return s.index(i)
        return -1
            