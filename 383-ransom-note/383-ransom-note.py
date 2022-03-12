from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x=Counter(ransomNote)
        y=Counter(magazine)
        for i,j in x.items():
            if i not in y:
                return False
            elif y[i]<j:
                return False
        return True
        