from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dit1=Counter(words1)
        dit2=Counter(words2)
        count=0
        for i in dit1:
            if dit1[i]==1 and i in dit2 and dit2[i]==1:
               count+=1
        return count