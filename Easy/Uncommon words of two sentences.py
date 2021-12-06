from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split(" ")
        s2=s2.split(" ")
        s=s1+s2
        dit=Counter(s)
        return [i for i,j in dit.items() if j==1]