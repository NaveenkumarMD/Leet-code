from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dit=Counter(arr)
        s=[i for i,j in dit.items() if j==1]
        k-=1
        if k>len(s)-1:
            return ""
        else:
            return s[k]