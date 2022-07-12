from collections import Counter
class Solution:
    def find(self,arr):
        dit=Counter(arr)
        for i in dit:
            if dit[i]>1:
                return False
        return True
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)-3+1):
            if self.find(s[i:i+3]):
                count+=1
        return count
        