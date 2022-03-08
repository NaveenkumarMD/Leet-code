from collections import Counter
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def normalform(s):
            return [s.find(i) for i in s]
        res=[]
        x=normalform(pattern)
        for i in words:
            if normalform(i)==x:
                res.append(i)
        return res
            